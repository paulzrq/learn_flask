{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "534c8453",
   "metadata": {},
   "outputs": [],
   "source": [
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
   "execution_count": null,
   "id": "3c5d1044",
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
