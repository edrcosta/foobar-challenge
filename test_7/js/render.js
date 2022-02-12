const c = document.getElementById("game");
const context = c.getContext("2d");
const canvas = new SpellCanvas('game', null)

const fixDpi = (c) => {
    const styleHeight = +getComputedStyle(c).getPropertyValue("height").slice(0, -2)
    const styleWidth = +getComputedStyle(c).getPropertyValue("width").slice(0, -2)
    c.setAttribute('height', styleHeight * window.devicePixelRatio)
    c.setAttribute('width', styleWidth * window.devicePixelRatio)
}

const drawLine = (context, { start: [x, y], end: [bx, by] }, color) => {
    color = color ? color : 'red'
    context.beginPath();
    context.moveTo(x, y);
    context.lineTo(bx, by);
    context.lineWidth = 1;
    context.strokeStyle = 'red';
    context.stroke();
}