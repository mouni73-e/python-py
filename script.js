/*
let course = ["pfsd","jfsd","mern",1,true,false];

console.log(course);
console.log(typeof(course));
console.log(course[0]);
console.log(course[1]);
console.log(course[2]);
console.log(course[3]);
console.log(course[4]);
*/
//execution content
//1.memory phase - variable environment
//2.code - thred of environment

/*
createCourse('jfsd');
console.log(m)

function createCourse(coursename){
    console.log("creating" + coursename);
}

var m = 10;
console.log(m)
createCourse('pfsd');

var a = 100;
console.log(a);
console.log(this.a)
console.log()
*/

/*
function hello(){
    const x = 10;
}
console.log(x);
hello();
*/
/*
 let a = function add(a,b){
    return a+b
}

let b = function sub(a,b){
    return a-b

}

function operate(operationFunc,a,b){
    operateFunc(a,b)
}


console.log(a(2,3));
console.log(b(2,3));

*/

/*

let a = 10;
function outer(){
    a = 100;
    function inner(){
        console.log(a);
    }
    return inner;
}

let returnFunc = outer();
a = 20;
console.log(returnFunc);
returnFunc();*/

function fetchData(callback){
    setTimeout(() => {
        let data = 'fetch data';
        callback(data,null)
    } , 5000)
}

function handeldata(data , error){
    if(error){
        console.error(error)
    }else{
        console.log(data)
    }
}

fetchData(handeldata);






