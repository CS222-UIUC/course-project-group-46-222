from contextlib import redirect_stderr
from flask import Flask, redirect, url_for, render_template, request
import scrape
from flask import Blueprint