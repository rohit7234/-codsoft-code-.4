{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMNbeNUSrk9AJia4VTnLzd5",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/rohit7234/-codsoft-code-.4/blob/main/subbu.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "print(\"hello\")"
      ],
      "metadata": {
        "id": "f2GMYVXwvHvR"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func():\n",
        "  print(\"hello world\")\n",
        "my_func()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mbcuZOYkvg-6",
        "outputId": "0161864c-465f-4770-d442-e11b511b01cb"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "hello world\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func(fname):\n",
        "  print(\"this is \" + fname)\n",
        "my_func(\"subbu\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WFxkCrWivsuy",
        "outputId": "7f6ceef2-5667-4bb2-c046-d7139f6b328f"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "this is subbu\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func(a,b,c):\n",
        "  if(a>b>c):\n",
        "    print(\"a is grater than b and c\")\n",
        "  elif(b>a>c):\n",
        "    print(\"b is grater than a and c\")\n",
        "  else:\n",
        "    print(\"c is grater than a and b\")\n",
        "my_func(2,3,4)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1upXHH7iwUZA",
        "outputId": "f1603f7f-a029-4bf0-e495-7c3e678b86ca"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "c is grater than a and b\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func():\n",
        "  apple=[\"banana\",\"pine apple\",\"carrot\"]\n",
        "  print(apple)\n",
        "my_func()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "r1iIXcpyy2L1",
        "outputId": "a35156de-b913-4f53-d621-a3a57bb09ebc"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['banana', 'pine apple', 'carrot']\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func():\n",
        "  apple=[\"banana\",\"a\",\"d\",\"er\",23,\"wer\"]\n",
        "  print(apple[0])\n",
        "my_func()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "g8eTkIkj0Moi",
        "outputId": "925d9669-38d3-424e-a0b6-16339cb4a118"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "banana\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func():\n",
        "  apple=[\"banana\",\"a\",\"d\",\"er\",23,\"wer\"]\n",
        "  print(apple.pop(2))\n",
        "my_func()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ftR0Q-T61K8X",
        "outputId": "b42ed24b-3997-46d0-e3c6-bfd9e27d9ddd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "d\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func(n):\n",
        "  fibonaci=[0,1]\n",
        "  for i in range(2,n):\n",
        "    fibonaci.append(fibonaci[-1]+fibonaci[-2])\n",
        "    print(fibonaci)\n",
        "my_func(5)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "if8_KGQI2EAQ",
        "outputId": "4687c736-5f65-4bd8-f3d8-8bfeda7bb585"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 1]\n",
            "[0, 1, 1, 2]\n",
            "[0, 1, 1, 2, 3]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def is_palindrome(s):\n",
        "    return s == s[::-1]\n",
        "\n",
        "print(is_palindrome(\"121\"))\n",
        "print(is_palindrome(\"121\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "melEI8lq67pr",
        "outputId": "80f5e9ba-21d6-498c-94d4-108c8cf45a33"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True\n",
            "True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def my_func(n):\n",
        "  subbu=[0,1]\n",
        "  for i in range(2,n):\n",
        "    subbu.append(subbu[-1]+subbu[-2])\n",
        "    print(subbu)\n",
        "my_func(10)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZJe2k62U7wL_",
        "outputId": "aeb3f2e8-428a-49d1-cbc4-e954b35b8428"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[0, 1, 1]\n",
            "[0, 1, 1, 2]\n",
            "[0, 1, 1, 2, 3]\n",
            "[0, 1, 1, 2, 3, 5]\n",
            "[0, 1, 1, 2, 3, 5, 8]\n",
            "[0, 1, 1, 2, 3, 5, 8, 13]\n",
            "[0, 1, 1, 2, 3, 5, 8, 13, 21]\n",
            "[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "sZoWjjHYCbHI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "VrxZCXNPDfwe"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}