import {config} from 'dotenv';
config()

import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

async function GFI() {
    words = document.getElementById("story");
    uni = document.getElementById("uni");
    genre = document.getElementById("genre");
    character = document.getElementById("character");

    if(ran == 0){
        if(character.value != ""){
            const completion = await openai.chat.completions.create({
                messages: [{ role: "system", content: "Create a fan fiction in the "+ genre.value +" genre in the " + uni.value + " universe, staring " + character.value }],
                model: "gpt-3.5-turbo",
                max_tokens: 3,
            });
        }
        else{
            const completion = await openai.chat.completions.create({
                messages: [{ role: "system", content: "Create a fan fiction in the "+ genre.value +" genre in the " + uni.value + " universe" }],
                model: "gpt-3.5-turbo",
                max_tokens: 3,
            });
        }
    }
    
    //alert
  
    words.innerHTML = completion.choices[0].message.content;
}