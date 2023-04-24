

let msg = new SpeechSynthesisUtterance();
let voices = speechSynthesis.getVoices();
msg.voice = voices[0];
// const tf = require('@tensorflow/tfjs');
let tags = document.querySelectorAll('p,h1,h2,h3'); // add more tags for you project
tags.forEach((tag) => {
    tag.addEventListener('click', (e) => {
        
        msg.text = e.target.innerText;
        
        speechSynthesis.speak(msg);
        
        let interval = setInterval(() => {
            if(!speechSynthesis.speaking){
                
                clearInterval(interval);
            }
        }, 100);

        tag.addEventListener('shiftKey', (e) => {
            msg.addEventListener('pause', (e) => {
                speechSynthesis.speak('Speech is being paused...');
            })
        })

        tag.addEventListener('click', (e) => {
            msg.addEventListener('resume', (e) => {
                speechSynthesis.speak(msg);
            })
        })
        
    });
});


let links = document.querySelectorAll('a, button'); // add more tags for you project
links.forEach((link) => {
    link.addEventListener('mousemove', (e) => {
        
        msg.text = e.target.innerText;
        
        speechSynthesis.speak(msg);
        
        
        let interval = setInterval(() => {
            if(!speechSynthesis.speaking){
                
                clearInterval(interval);
            }
        }, 100);

        
        
    });
});

var imgs = document.querySelectorAll('img');
imgs.forEach((img) => {
    img.addEventListener('click', (e) => {
        msg.text = e.target.alt;
        
        speechSynthesis.speak(msg);
        
        
        let interval = setInterval(() => {
            if(!speechSynthesis.speaking){
                
                clearInterval(interval);
            }
        }, 100);

    });
});

  



