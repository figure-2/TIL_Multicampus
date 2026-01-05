let myHeading = document.querySelector("h1");  
myHeading.textContent = "Hello world!";

// 변수 선언
let myVariable

// 값 할당
myVariable = 'hello'

console.log(myVariable)

let myVariable2 = 'world'

console.log(myVariable2)

var a = 1  // 옛날에 사용한 것이기 때문에 사용 거의 안함

let b = 2  // 변경이 가능한 데이터일 때 사용(재할당 가능)
const c = 3  // 데이터 변형이 없어야할 때/ 변경이 불가능한 데이터일 때 사용(재할당 막음)

console.log(a,b,c)

a = 10
b = 20
// const 로 선언된 변수는 재할당 불가능
// c = 30

var a = 100
// let, const로 선언된 변수는 재선언 불가능
// let b = 200  // 같은 영역안에 b와 c라는 변수를 또 선언하는 것은 불가능
// const c = 300

// type
let stringVar = 'hello'
let numberVar = 10
let boolVar = true
let arrayVar = []
let objectVar = {}

console.log(stringVar, numberVar, boolVar, arrayVar, objectVar)

arrayVar.push('hello')
console.log(arrayVar)

objectVar.name = 'kim'
objectVar.location = 'seoul'
console.log(objectVar)

// my_dict = Object()
let myObject = new Object()  // 인스턴스화 하는데 앞에 new를 붙여줘야함
myObject.name = 'park'

console.log(myObject)

// 연산자
let myVarA = 10
let myVarB = '10'

console.log(myVarA == myVarB)  // 좋지 않은 동작
console.log(myVarB === myVarB)  // 웬만하면 === 로 같은지 비교

// 조건문
// let iceCream = 'chocolate'
// if (iceCream === 'chocolate') { // {} 중가로를 사용하여 함수 내부에 있는 것을 뜻함
//     alert('choco') // alert : 팝업을 띄어줌(알림보내줌)
// }   else {
//     alert('no choco')
// }

// 반복문
console.log('while')
let i = 0
while (i < 5){
    console.log(i)
    i++ // python => i += 1
}

console.log('for')
for (let i=0; i<5; i++){
    console.log(i)
}

console.log('for2')
let myArray = [1,2,3,4,5]
for (let i=0; i<myArray.length; i++){
    console.log(myArray[i])
}

console.log('for in')   // 인덱스를 추출
// for item in myArray:
for (let item in myArray){
    console.log(item)   // => 결과값 : 0,1,2,3,4
}

console.log('for of')  // 많이 사용 2
for (let item of myArray){
    console.log(item)   // => 결과값 : 1,2,3,4,5
}

console.log('for each')  // 많이 사용 1
myArray.forEach(function(item, index, array){
    console.log(array) // item : 1,2,3,4,5 / index: 0,1,2,3,4 / array : (5) [1,2,3,4,5]
})

// 함수

//def multi():
function multiply(num1, num2){  // 직접 console 창에다가 multiply(5,10) 작성
    let result = num1*num2
    console.log(this) // this : 지금 이 객체안에 있는 자기자신(= self)
    return result
}
console.log(multiply(3,4))

// 함수 표현식
let multiply2 = function (num1, num2){  // 함수 만들고 변수에 넣기
    let result = num1 * num2
    console.log(this)
    return result
}
console.log(multiply2(3,4))

// 화살표 함수
let multiply3 = (num1, num2) => {   // () => {} function 키워드 제외하고 화살표로 작성
    let result = num1 * num2
    console.log(this)
    return result
} 
console.log(multiply3(3,4))

// 화살표 함수 생략 1
// {}안의 코드가 return 하는 문장 하나만 있을 때 {}와 return 생략가능
let multiply4 = (num1, num2) => {
    return num1 * num2
}

let multiply4_1 = (num1, num2) => num1 * num2


// 화살표 함수 생략 2
// ()안에 매개변수가 하나만 있다면 ()를 생략가능
let multiply5 = (num1) => num1 * 2

let multiply5_1 = num1 => num1 * 2


let testObj = {
    mul1 : multiply,  // 함수
    mul2 : multiply2, // 함수
    mul3 : multiply3  // 화살표함수
}


// 이벤트
document.querySelector('html').onclick = function(){
    // alert('hihi')
}

document.querySelector('h1').onclick = function(){
    // alert('hihi')
}

// 이벤트 리스너
// - h1태그를 클릭시   
// let myH1 = document.querySelector('h1') 
// // addEventListener(무슨일이 일어 났을때, 무슨 행동을 할지)
// myH1.addEventListener('click', function(e){
//     // alert('hello')
//     console.log('hihi')
//     console.log(e)
// })

// - h1태그에 마우스를 올렸을 때
let myH1 = document.querySelector('h1') 
// addEventListener(무슨일이 일어 났을때, 무슨 행동을 할지)
myH1.addEventListener('mouseover', function(e){
    // alert('hello')
    console.log('hihi')
    console.log(e)
})

// - image를 클릭시 사진 변경
let myImage = document.querySelector('img')
console.log(myImage) // 잘 찾아진건지 확인

myImage.addEventListener('click', function(){
    let src = myImage.getAttribute('src') // 속성을 가져와
    console.log(src)
    if (src === 'images/firefox-icon.png'){
        myImage.setAttribute('src', 'images/푸바옹.jpg') //속성을 바꿔
    } else{
        myImage.setAttribute('src', 'images/firefox-icon.png')
    }
})

// 비동기 : 작업이 돌발적으로 들어올 때 처리 => JS가 비동기에 해당
// 동기 : 작업이 시작하고 끝나기전에는 아무일도 못하는것

console.log('hi')
// setTimeout(실행시킬함수, 시간)
setTimeout(function(){console.log('??')}, 2000)  // 2초뒤에 실행

console.log('bye')

// => 결과 hi, bye, ??

// 어떤 버튼을 눌렀을 때
// google 서버에서 사진(4gb)을 한장 다운받아서
// 화면에 출력


// - 비동기처리로 API요청보냄
const URL = 'https://jsonplaceholder.typicode.com/posts/1'

// 비동기처리 오류발생 O
// let response = fetch(URL)
// let result = response.json()
// console.log(response)
// console.log(result) // -> 오류

// 비동기처리 오류발생 X 
// - 방법1
fetch(URL)  // fetch() : 비동기
    .then( response => response.json())
    .then(json => console.log(json))

// - 방법2
async function fetchAndPrint(){  // async : 비동기적인 코드가 들어가있음을 알림.
    let response = await fetch(URL) // await : fetch(URL)할 때까지 기다림.
    let result = await response.json()

    console.log(result)
}
fetchAndPrint()


// 모든 li태그를 모아서 변수에 집어넣을 것
const liElements = document.querySelectorAll('li')
console.log(liElements)  // 결과값 : NodeList(3) [li, li, li]

// 모은 li태그로 하나씩 출력
for (const li of liElements){
    console.log(li)
}

// 꾸미기
liElements.forEach(function(li){
    li.style.color = 'red'
    li.style.backgroundColor = 'blue'
})

// 서로 같은 동작
// liElements.forEach(function(li){
//     li.addEventListener('click',function(){
//         console.log('hello')
//     })
// })

// 서로 다른 동작
liElements.forEach(function(li){
    li.addEventListener('click',function(e){
        console.log(e)
        console.log(e.target)
        console.log(e.target.textContent)

        if (e.target.textContent === 'thinkers'){
            e.target.style.color = 'black'
        }
    })
})

// fetch랑 연결해서 사용
