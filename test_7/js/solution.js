const solution = (dimensions, your_position, trainer_position, distance) => {
    
    psize = 100
    ii= 0
    for (let y = 0; y < dimensions[1]; y++) {
        for (let x = 0; x < dimensions[0]; x++) {
            canvas.drawPixel(x*psize, y*psize, ii%2==0 ? 'grey' : '#5e5e5e', psize, psize)
            ii++
        }
    }

    canvas.drawPixel(your_position[0]*psize, your_position[1]*psize, 'blue', 10, 10)
    canvas.drawPixel(trainer_position[0]*psize, trainer_position[1]*psize, 'green', 10, 10)

    end = [0, 0]

    drawLine(context, {
        start: [your_position[0]*psize, your_position[1]*psize],
        end: [end[0], end[1]],
    })


    terceiro = [end[0] + your_position[0], 0]
    canvas.drawPixel(terceiro[0]*psize, terceiro[1]*psize, 'blue', 10, 10)
    canvas.drawPixel(end[0]*psize, end[1]*psize, 'blue', 10, 10)


    

    console.log(fire_size)
}

solution([3,2], [1,1], [2,1], 4)
