package com.example.anagram

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.Toast
import android.widget.EditText

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        // our code
        val btn = findViewById<Button>(R.id.button)
        val input = findViewById<EditText>(R.id.edittextinput)
        val minLetters:Int = 3
        val maxLetters:Int = 15

        findViewById<Button>(R.id.button).setOnClickListener { view ->
            var msg:String = ""
            val inputText:String? = input.text.toString()
            val ctn:Int? = inputText?.length
            if (ctn != null) {
                if (ctn >= minLetters && ctn <= maxLetters) {
                    msg = "Your word is: $inputText"
                } else {
                    msg = "You need to provide a word between $minLetters & $maxLetters"
                }
            } else {
                msg = "Please provide a word"
            }
            Toast.makeText(this, msg, Toast.LENGTH_LONG).show()
        }
    }

}