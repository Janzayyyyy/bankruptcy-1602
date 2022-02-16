{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import request, render_template\n",
    "from keras.models import load_model\n",
    "\n",
    "@app.route(\"/\", methods=[\"GET\", \"POST\"])\n",
    "def index():\n",
    "    if request.method==\"POST\":\n",
    "        NPTA = request.form.get(\"NPTA\")\n",
    "        TLTA = request.form.get(\"TLTA\")\n",
    "        WCTA = request.form.get(\"WCTA\")\n",
    "        print(NPTA, TLTA, WCTA)\n",
    "        model = load_model(\"bankruptcy_model\")\n",
    "        pred = model.predict([[float(NPTA), float(TLTA), float(WCTA)]])\n",
    "        s = \"The predicted bankruptcy score is \" + str(pred)\n",
    "        return(render_template(\"index.html\", result=s))\n",
    "    else:\n",
    "        return(render_template(\"index.html\", result=\"2\"))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
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
      "127.0.0.1 - - [16/Feb/2022 17:38:14] \"\u001b[37mGET / HTTP/1.1\u001b[0m\" 200 -\n",
      "127.0.0.1 - - [16/Feb/2022 17:38:14] \"\u001b[33mGET /favicon.ico HTTP/1.1\u001b[0m\" 404 -\n"
     ]
    }
   ],
   "source": [
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
