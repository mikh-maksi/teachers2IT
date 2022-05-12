function check_f() {
    let a_val = parseInt(a.value);
    let b_val = parseInt(b.value);
    let compare_val = compare.value;
    let result = 0;
    if ((a_val > b_val) && (compare_val == '>')) {
        console.log("Ok");
        result = 1;
    }
    if ((a_val < b_val) && (compare_val == '<')) {
        console.log("Ok");
        result = 1;
    }
    if ((a_val == b_val) && (compare_val == '=')) {
        console.log("Ok");
        result = 1;
    }

    if (result) {
        alert("Right answer!");
    } else {
        alert("Wrong Answer!");
    }

    console.log(a_val, b_val, compare_val);

}

function new_f() {
    console.log("new");
    a.value = getRandomInt(10);
    b.value = getRandomInt(10);
}

function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

b_check.addEventListener("click", check_f);
b_new.addEventListener("click", new_f);