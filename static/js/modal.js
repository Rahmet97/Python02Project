const modal = document.querySelector(".modal")
const xSVG = document.querySelector(".xSVG")
const vacancies = document.querySelectorAll(".vacancy")

vacancies.forEach(vacancy => {
    vacancy.addEventListener("click", () => {
        modal.classList.remove("display-none")
        body.classList.add("overflow-y-hidden")
    })
})

xSVG.addEventListener("click", () => {
    modal.classList.add("display-none")
    body.classList.remove("overflow-y-hidden")
})

modal.addEventListener("click", () => {
    modal.classList.add("display-none")
    body.classList.remove("overflow-y-hidden")
})