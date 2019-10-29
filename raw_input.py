{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled1.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python2",
      "display_name": "Python 2"
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
        "<a href=\"https://colab.research.google.com/github/mgwmendes/curso-iintorducao_pyton/blob/master/raw_input.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "eei7DwoYBmYh",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 68
        },
        "outputId": "d583f72f-9cb6-4dc2-9793-6a8d7fdbf922"
      },
      "source": [
        "def cadastrar(nomes):\n",
        "  print('Digite o nome :')\n",
        "  nome = raw_input()\n",
        "  nomes = nomes.append(nome)\n",
        "\n",
        "\n",
        "nomes=[]\n",
        "cadastrar(nomes)  \n",
        "\n",
        "print(nomes)\n",
        " "
      ],
      "execution_count": 84,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Digite o nome :\n",
            "Mendes\n",
            "['Mendes']\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}