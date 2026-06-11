import boto3


def test_aws_connection():
    # 1. Connect to the S3 service using the credentials stored on your computer
    s3 = boto3.client('s3', region_name='us-east-1')

    try:
        # 2. Request a list of all your S3 buckets from Amazon
        print("Connecting to AWS...")
        response = s3.list_buckets()

        print("\n🎉 SUCCESS! Your PyCharm is perfectly connected to AWS.")
        print("Here are your current S3 storage lockers:")

        # 3. Print out the names of your buckets
        for bucket in response['Buckets']:
            print(f" -> {bucket['Name']}")

    except Exception as e:
        print("\n❌ Connection failed.")
        print(f"Error details: {e}")


# This tells Python to run our function immediately when we hit play
if __name__ == "__main__":
    test_aws_connection()