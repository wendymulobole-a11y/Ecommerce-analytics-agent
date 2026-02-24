# MCP-Powered BigQuery Analytics Agent  
**Google ADK + Gemini + MCP Toolbox**

## Overview

This project implements a production-style natural language analytics agent using Google ADK, Gemini, and the MCP Toolbox for Databases.

The agent answers user questions about the public BigQuery dataset:

`bigquery-public-data.thelook_ecommerce`

Instead of generating arbitrary SQL, the system uses predefined, parameterized BigQuery tools exposed through MCP. This ensures:

- Read-only execution
- Dataset-level restriction
- No dynamic or destructive SQL
- Secure separation between reasoning and execution

The result is a safe, tool-driven analytics interface powered by an LLM.

---

## Architecture

User  
↓  
Gemini (ADK LlmAgent)  
↓  
MCP Toolbox (BigQuery tools)  
↓  
BigQuery  
↓  
Structured response  

### Design Principles

- Tool-based execution model
- No dynamic SQL generation
- Dataset restricted via `allowedDatasets`
- Parameterized queries only
- Read-only analytics design

The LLM handles reasoning and tool selection.  
MCP handles database execution.  
BigQuery performs query processing.

---

## Implemented Tools

### 1. total-orders
Returns total number of orders.

### 2. revenue-by-date-range
Calculates total revenue between two dates.

Parameters:
- start_date (YYYY-MM-DD)
- end_date (YYYY-MM-DD)

### 3. top-products
Returns top N products ranked by revenue.

Parameter:
- limit (integer)

All tools are implemented using `bigquery-sql` with predefined SQL statements.

---

## Example Queries

**How many total orders do we have?**

**What was revenue between 2024-01-01 and 2024-01-31?**

**Show me the top 5 products by revenue.**

---

## Safety Model

Safety is enforced at multiple layers:

- Dataset restriction via MCP configuration
- No mutation statements (no INSERT, UPDATE, DELETE)
- Parameter binding using `@param` syntax
- LLM cannot directly access BigQuery
- All execution flows through MCP

This mirrors enterprise-safe AI system design patterns.

---

## Setup

### 1. Requirements

- Python 3.10+
- Google ADK
- MCP Toolbox for Databases
- BigQuery service account credentials

---

### 2. Set Credentials
export GOOGLE_APPLICATION_CREDENTIALS="path/to/service_account.json"
Service account should have:

roles/bigquery.user

roles/bigquery.dataViewer

### 3. Start MCP Toolbox

./toolbox --tools-file tools.yaml

This starts MCP (default example: http://localhost:5000).

### 4. Run ADK Web

In a separate terminal:

adk web

Open the web interface (typically http://localhost:8000) and start querying the agent.

---

## Technologies Used

Google ADK

Gemini 2.5 Flash

MCP Toolbox for Databases

BigQuery

Python

---

## This project demonstrates:

Secure LLM-to-database orchestration

Tool-based reasoning architecture

Cloud-native analytics integration

Production-aligned AI system design

It reflects how modern enterprise AI systems safely integrate LLMs with structured data systems.
