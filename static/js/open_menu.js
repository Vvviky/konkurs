let nvrightmedia = document.querySelector(".nvrightmedia");
nvrightmedia.onclick = function (){
    let nvright = document.querySelector(".nvright");
    if (nvright.classList.contains("show"))  {
        nvright.classList.remove("show");
    }
    else {
        nvright.classList.add("show");
    }
}