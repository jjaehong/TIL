// for..in vs for..of

const arr = []
arr[4] = 4
arr[1] = 1
arr[2] = 2

// 배열을 순회할때는 in 사용 xxxx
for (const i in arr) {
  console.log(i)
}

console.log("============")

for (const i of arr) {
  console.log(i)
  
}