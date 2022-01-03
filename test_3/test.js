(() => {
    arr = [4, 3, 1, 2, 5]
    let swapCount = 0
    for(let i = 0;i < arr.length;i++){
        while(arr[i] !== i+1){
            const temp = arr[i]
            arr[i] = arr[temp -1]
            arr[temp -1] = temp
            swapCount++
        }
    }
    console.log(arr)



})()