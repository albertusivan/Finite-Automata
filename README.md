#Cara menggunakan Program Lexical Analyzer

1. Program dapat menerima inputan berupa string.
2. Terdapat 10 kata yang akan dinyatakan valid ketika diinput ke dalam Lexical Analyzer diantaranya.
    - mother
    - father
    - eating
    - wearing
    - playing
    - jacket
    - jeans
    - game
    - sushi
    - noodle
3. Jika terdapat inputan diluar 10 kata diatas program akan mengeluarkan output error.
4. Program dapat menerima inputan dalam bentuk kalimat (gabungan beberapa kata diatas).
5. Jika terdapat kata dalam kalimat yang diinputkan tidak terdaftar dalam 10 kata diatas, program akan mengeluarkan output error.

**Cara menggunakan Program Lexical Analyzer**

1. Program dapat menerima inputan berupa string.
2. Terdapat 10 kata yang akan dinyatakan valid ketika diinput ke dalam Lexical Analyzer diantaranya.
    - mother
    - father
    - eating
    - wearing
    - playing
    - jacket
    - jeans
    - game
    - sushi
    - noodle
3. Jika terdapat inputan diluar 10 kata diatas program akan mengeluarkan output error.
4. Program dapat menerima inputan dalam bentuk kalimat (gabungan beberapa kata diatas).
5. Jika terdapat kata dalam kalimat yang diinputkan tidak terdaftar dalam 10 kata diatas, program akan mengeluarkan output error.

**Cara menggunakan Program Parser**

1. Program dapat menerima inputan berupa kalimat yang terdiri dari kata di bawah ini.
    - mother [SU]
    - father [SU]
    - eating [VB]
    - wearing [VB]
    - playing [VB]
    - jacket [OB]
    - jeans[OB]
    - game [OB]
    - sushi [OB]
    - noodle [OB]
2. Program akan mengeluarkan output error jika terdapat kata dalam kalimat yang diinputkan diluar 10 kata diatas.
3. Program akan mengeluarkan output error jika terdapat kalimat yang diinputkan tidak sesuai grammar [SU] [VB] [OB]
4. Program akan valid jika kata dalam kalimat yang diinputkan diluar berada dalam list 10 kata diatas dan sesuai grammar [SU] [VB] [OB]
