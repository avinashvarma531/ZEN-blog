// gsap.registerPlugin(ScrollTrigger);

// gsap.from('.post', {
//     opacity: 0,
//     // scale: 0.6,
//     xPercent: -50,
//     duration: 1,
//     stagger: 0.2,
//     scrollTrigger:{
//         trigger: '.post-container',
//         start: "top 95%",
//         end: "bottom top",
//         markers: true
//     }
// })
const bck = document.getElementById('back-button');
bck.addEventListener('click', ()=>{
    console.log('Hello');
    window.history.back();
})