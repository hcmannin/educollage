const wrapper = document.querySelector(".search-sec"),
selectBtn = wrapper.querySelector(".select-btn");

selectBtn.addEventListener("click", () => {
    wrapper.classList.toggle("active");
});