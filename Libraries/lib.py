from datasets import load_dataset
from pinecone import Pinecone, ServerlessSpec
from tqdm.auto import tqdm
import ast
import pandas as pd
from google.genai.types import HttpOptions
import google.genai as genai
from google.genai.types import GenerateContentConfig, Part
from pinecone import SearchQuery
from pinecone import Pinecone
import os
import sys
from pathlib import Path

