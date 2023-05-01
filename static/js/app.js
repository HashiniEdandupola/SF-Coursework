/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    
    burger.addEventListener('click',() => {
       nav.classList.toggle('nav-active');
       
       navLinks.forEach((link, index)=>{
        if(link.style.animation)
        {
            link.style.animation='';           
        }
        else
        {
            link.style.animation = `navLinkFade 1s ease forwards ${index / 2}s`;
        }
    });
    burger.classList.toggle('toggle');
  });

};

navSlide();