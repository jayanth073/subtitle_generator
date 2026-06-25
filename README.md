# Automated Video/Audio Subtitle Generator using AWS

A cloud-native, serverless, event-driven pipeline that automatically processes audio/video files to generate structured subtitle files (`.srt`). Built using **Python (Boto3)** and hosted entirely on **Amazon Web Services (AWS)**, this architecture leverages an asynchronous AI-driven speech-to-text engine to compute word-level millisecond boundaries natively in the cloud.

---

##  Architecture Overview

The platform uses a decoupled, serverless microservices workflow designed for high scalability and zero idle-cost infrastructure:

1. **Audio Storage Ingestion:** Media tracks (`.mp3`) are uploaded directly to an **Amazon S3** ingress bucket.
2. **Transcription Layer:** An S3 Object Creation Event automatically triggers the **`StartTranscription` Lambda function**, which maps the storage reference path and invokes an asynchronous processing job inside **AWS Transcribe**.
3. **Subtitle Conversion Layer:** Upon completion, AWS Transcribe delivers a raw timestamped payload (`.json`) back to the bucket. This secondary drop triggers the **`ConvertJsonToSrt` Lambda function**.
4. **Data Engineering Output:** The secondary function streams the file contents, computes textual line breaks based on punctuation markers, formats the temporal segments into standard `HH:MM:SS,mmm` layouts, and commits a clean `.srt` track back to S3.
5. **Observability:** Performance execution logs, latency tracking, and cloud compute metrics are funneled directly into **AWS CloudWatch Logs**.

---

## 🛠️ Tech Stack & Services

* **Cloud Platform:** Amazon Web Services (AWS)
* **Compute Engine:** AWS Lambda (Runtime: Python 3.12)
* **AI/ML Service:** AWS Transcribe (Automatic Speech Recognition)
* **Storage Layer:** Amazon S3 (Simple Storage Service)
* **Monitoring Tool:** AWS CloudWatch Logs
* **SDK:** Boto3 (AWS SDK for Python)

---

## 📂 Project Repository Structure

├── .gitignore                # Optimized exclusion matrix (ignores media, venv, and IDE files)
├── main_lambda_1.py          # Lambda function code for triggering AWS Transcribe
├── main_lambda_2.py          # Lambda function code for parsing JSON into standard SRT
└── README.md                 # Project system documentation
