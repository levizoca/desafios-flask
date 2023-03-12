let list = document.getElementById("list");

function addItem() {
    let item = document.getElementById("input-box").value;

    if (item === "") {
        alert("Please enter an item!");
    } else {
        let li = document.createElement("li");
        let span = document.createElement("span");
        let div = document.createElement("div");
        div.classList.add("buttons");
        span.innerText = item;
        li.appendChild(span);
        li.appendChild(div);

        let editButton = document.createElement("button");
        editButton.innerText = "Edit";
        editButton.onclick = function () {
            editItem(li);
        };
        div.appendChild(editButton);

        let deleteButton = document.createElement("button");
        deleteButton.innerText = "Delete";
        deleteButton.onclick = function () {
            deleteItem(li);
        };
        div.appendChild(deleteButton);

        list.appendChild(li);
        document.getElementById("input-box").value = "";
    }
}

function deleteItem(item) {
    item.parentNode.removeChild(item);
}

function editItem(item) {
    let newItem = prompt("Enter new item:");
    if (newItem === "") {
        alert("Please enter an item!");
    } else {
        item.firstChild.innerText = newItem;
    }
}