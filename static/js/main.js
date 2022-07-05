const arrowLink = document.querySelector(".arrowLink")
const projectLink = document.querySelector(".projectLink")
const projectSVG = document.querySelector(".projectSVG")
const serviceLink = document.querySelector(".serviceLink")
const serviceSVG = document.querySelector(".serviceSVG")
const langLink = document.querySelector(".langLink")
const langSVG = document.querySelector(".langSVG")

const mobileHeaderContainer = document.querySelector(".mobileHeaderContainer")
const body = document.querySelector(".body")
const hamburger = document.querySelector("#hamburger")
const mobileHeader = document.querySelector(".mobileHeader")

const span1 = document.querySelector("#span1")
const span2 = document.querySelector("#span2")
const span3 = document.querySelector("#span3")

hamburger.addEventListener("click", () => {
    body.classList.toggle("overflow-y-hidden")
    mobileHeader.classList.toggle("hidden")
    mobileHeader.classList.toggle("flexCenter")
    span1.classList.toggle("rotate45deg")
    span2.classList.toggle("hidden")
    span3.classList.toggle("rotate-45deg")
})

projectLink.addEventListener("mouseover", () => {
    projectSVG.classList.add("rotate")
})

projectLink.addEventListener("mouseout", () => {
    projectSVG.classList.remove("rotate")
})

serviceLink.addEventListener("mouseover", () => {
    serviceSVG.classList.add("rotate")
})

serviceLink.addEventListener("mouseout", () => {
    serviceSVG.classList.remove("rotate")
})

langLink.addEventListener("mouseover", () => {
    langSVG.classList.add("rotate")
})

langLink.addEventListener("mouseout", () => {
    langSVG.classList.remove("rotate")
})

window.addEventListener("scroll", scrollHeader)

function scrollHeader() {
    const scrollHeader = document.querySelector(".scrollHeader")
    if (this.scrollY >= 150) {
        scrollHeader.classList.remove("hidden")
    } else {
        scrollHeader.classList.add("hidden")
    }   
}

const serviceLinkScroll = document.querySelector(".serviceLinkScroll")
const serviceSVGScroll = document.querySelector(".serviceSVGScroll")
const projectLinkScroll = document.querySelector(".projectLinkScroll")
const projectSVGScroll = document.querySelector(".projectSVGScroll")
const langLinkScroll = document.querySelector(".langLinkScroll")
const langSVGScroll = document.querySelector(".langSVGScroll")

serviceLinkScroll.addEventListener("mouseover", () => {
    serviceSVGScroll.classList.add("rotate")
})

serviceLinkScroll.addEventListener("mouseout", () => {
    serviceSVGScroll.classList.remove("rotate")
})

projectLinkScroll.addEventListener("mouseover", () => {
    projectSVGScroll.classList.add("rotate")
})

projectLinkScroll.addEventListener("mouseout", () => {
    projectSVGScroll.classList.remove("rotate")
})

langLinkScroll.addEventListener("mouseover", () => {
    langSVGScroll.classList.add("rotate")
})

langLinkScroll.addEventListener("mouseout", () => {
    langSVGScroll.classList.remove("rotate")
})

// FOOOTER 
const toTopBtn = document.querySelector("#toTopBtn")

toTopBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    })
})

const currentYearSpans = document.querySelectorAll(".currentYear")
const currentYear = new Date().getFullYear()
currentYearSpans.forEach(currentYearSpan => {
    currentYearSpan.append(currentYear)
}) 

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 1,
    navigation: {
        nextEl: ".nextEl",
        prevEl: ".prevEl",
    },
    breakpoints: {
        640: {
            slidesPerView: 1.5,
        },
        920: {
            slidesPerView: 2.5,
        }
    }
  });