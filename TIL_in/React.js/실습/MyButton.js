

const MyButton = function (props) {
  const [isClicked, setIsClicked] = React.useState(false)

  return React.createElement(
    'button',
    { onClick: () => {setIsClicked(true)} },
    isClicked ? '클릭했어!' : '여기를 클릭해!'
  )
}

const domContainer = document.querySelector('#root')
ReactDOM.createRoot(React.createElement(MyButton), domContainer)