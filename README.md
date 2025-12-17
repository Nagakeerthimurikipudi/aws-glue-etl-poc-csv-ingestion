# AWS Glue ETL PoC – CSV Ingestion

This repository contains a proof of concept (PoC) demonstrating batch-based CSV ingestion using AWS Glue. The objective of this PoC is to evaluate offloading file-based processing from on-prem ETL servers.

## Problem Statement
On-prem Informatica servers had restrictions and performance constraints for file-based ETL processing. A PoC was conducted to assess AWS-based batch ingestion as an alternative.

## Architecture Overview
- Source: CSV files from upstream systems
- Storage: Amazon S3
- Processing: AWS Glue (PySpark)
- Target: PostgreSQL database
- Downstream: Informatica PowerCenter ETL pipelines

## ETL Flow
1. CSV files are staged in Amazon S3
2. AWS Glue job reads CSV files
3. Deduplication applied using business keys and timestamps
4. Incremental records identified using ingestion timestamps
5. Processed data loaded into PostgreSQL inbound tables
6. Downstream Informatica jobs consume the data

## Key Features
- File-level deduplication
- Incremental processing
- Batch-oriented ETL design
- Compatible with existing Informatica workflows

## Notes
This PoC is designed for evaluation and learning purposes and does not represent a full production deployment.
