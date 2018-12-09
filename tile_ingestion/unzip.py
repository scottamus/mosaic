import zipfile
import boto3
import io


def unzip():
    session = boto3.session.Session(profile_name="default")
    s3 = session.resource("s3")
    bucket = s3.Bucket('scottamus-mosaic')
    obj = bucket.Object('tilesupload/test_files.zip')  # how do I pass this in?

    with io.BytesIO(obj.get()["Body"].read()) as tf:

        # rewind the file
        tf.seek(0)

        # Read the file as a zipfile and process the members
        with zipfile.ZipFile(tf, mode='r') as zipf:
            for subfile in zipf.namelist():
                print(subfile)


if __name__ == "__main__":
    print("+================+")
    print("|  Hello world!  |")
    print("+================+")
