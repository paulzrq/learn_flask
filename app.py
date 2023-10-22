{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "617464b0",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Writing run.py\n"
     ]
    }
   ],
   "source": [
    "%%writefile run.py\n",
    "from flask import Flask\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/')\n",
    "def hello():\n",
    "    return 'Welcome to My Watchlist!'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "0d6897d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<Popen: returncode: None args: 'FLASK_APP=run.py flask run'>"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"run.py\"\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n",
      "127.0.0.1 - - [21/Oct/2023 23:36:45] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [21/Oct/2023 23:36:45] \"GET /favicon.ico HTTP/1.1\" 404 -\n"
     ]
    }
   ],
   "source": [
    "import subprocess as sp\n",
    "\n",
    "server = sp.Popen(\"FLASK_APP=run.py flask run\", shell=True)\n",
    "server"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c751ddb6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b92e20b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
