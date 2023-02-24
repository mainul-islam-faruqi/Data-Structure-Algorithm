function linear_search(array, x) {
  for (let i=0; i < array.length; i++) {
    if (array[i] === x) {
      return i
    }
  }
  const i = -1;
  return i
}
console.log(linear_search([1,2,4, 12, 33, 44, 55, 77, 90, 45], 44))