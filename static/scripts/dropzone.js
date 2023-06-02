document.querySelectorAll(".drop-zone__input").forEach(dropZoneInput => {
    const dropZone = dropZoneInput.closest(".drop-zone");

    // Changes border-style when file is dragged over dropZone
    dropZone.addEventListener("dragover", e => {
        e.preventDefault();
        dropZone.classList.add("drop-zone--over");
    });

    // Reverts change to border-style upon leaving
    ["dragleave", "dragend"].forEach(type => {
        dropZone.addEventListener(type, function() {
            dropZone.classList.remove("drop-zone--over");
        });
    });

    // Upon dropping an element into dropZone, copies file(s) to dropZoneInput
    dropZone.addEventListener("drop", e => {
        e.preventDefault();
        if (e.dataTransfer.files.length) {
            dropZoneInput.files = e.dataTransfer.files;
            updateThumbnail(dropZone, e.dataTransfer.files);
        };
        dropZone.classList.remove("drop-zone--over");
    });

    // Handles clicks on dropZone
    dropZone.addEventListener("click", function() {
        dropZoneInput.click();
        dropZoneInput.addEventListener('change', e => {
            console.log(e)
            const fileList = e.target.files
            if (fileList.length) {
                updateThumbnail(dropZone, fileList);
            };
        });
    });
});

function updateThumbnail(dropZone, fileList) {
    let file = fileList[0]
    let thumbnailElement = dropZone.querySelector(".drop-zone__thumb")

    // Removes prompt to make space for thumbnailElement
    if (dropZone.querySelector(".drop-zone__prompt")) {
        dropZone.querySelector(".drop-zone__prompt").remove();
    }

    // If thumbnailElement doesn't exist, create it and append to dropZone
    if (!thumbnailElement) {
        thumbnailElement = document.createElement("div");
        thumbnailElement.classList.add("drop-zone__thumb");
        dropZone.appendChild(thumbnailElement);
    }

    // Changes data-label to file name
    thumbnailElement.dataset.label = file.name;

    // Changes thumbnail image to dropped file
    if (file.type.startsWith("image/")) {
        const reader = new FileReader();

        reader.readAsDataURL(file);
        reader.onload = () => {
            thumbnailElement.style.backgroundImage = `url('${ reader.result }')`;
        }
    }
}