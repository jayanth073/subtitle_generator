import boto3
import time


def upload_and_transcribe():
    # Names of your files and bucket
    bucket_name = "subtitle-generator-personal"  # ⚠️ Make sure this matches your exact bucket name
    local_file = "KaikaiKitan.mp3"  # The file you just put in PyCharm
    cloud_file = "input_audio.mp3"  # What it will be named in S3
    job_name = f"SubtitleJob-{int(time.time())}"  # Unique name for the AI job

    # Initialize AWS clients
    s3 = boto3.client('s3', region_name='us-east-1')
    transcribe = boto3.client('transcribe', region_name='us-east-1')

    try:
        # Step 1: Upload the file to S3
        print(f"1. Uploading '{local_file}' to your S3 bucket...")
        s3.upload_file(local_file, bucket_name, cloud_file)
        print("   Uploaded successfully!")

        # Step 2: Trigger AWS Transcribe
        file_uri = f"https://s3.amazonaws.com/{bucket_name}/{cloud_file}"
        print(f"\n2. Sending file to AWS Transcribe AI...")
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={'MediaFileUri': file_uri},
            MediaFormat='mp4',
            LanguageCode='en-US'
        )

        # Step 3: Wait for the AI to finish
        print("3. Waiting for the AI to finish listening...")
        while True:
            status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
            job_status = status['TranscriptionJob']['TranscriptionJobStatus']

            if job_status == 'COMPLETED':
                transcript_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
                print("\n🎉 SUCCESS! AWS Transcribe has finished processing your audio.")
                print(f"Your raw subtitle data link:\n{transcript_url}")
                break
            elif job_status == 'FAILED':
                print("\n❌ Transcription job failed.")
                break

            print("   AI is still processing... checking again in 10 seconds.")
            time.sleep(10)

    except Exception as e:
        print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    upload_and_transcribe()