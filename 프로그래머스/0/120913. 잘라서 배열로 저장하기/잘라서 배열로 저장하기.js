function solution(my_str, n) {
    const myStr = []
    
    for (let i = 0; i < my_str.length; i += n) {
        myStr.push(my_str.slice(i, i + n))
    }
    
    return myStr
}