export default function two_crystal_balls(breaks: boolean[]): number {
    const jumpInterval = Math.floor(Math.sqrt(breaks.length)); // we will jump a sqrt of n times to find where does the ball break

    let i = jumpInterval; // start at the sqrt of n

    for (; i < breaks.length; i += jumpInterval) { // start to jump through the breaks 
        if (breaks[i])
            break;
    } // find a spot that breaks, so we only have one more ball

    i -= jumpInterval; // step back where it doesnt break

    for (let j = 0; j <= jumpInterval && i < breaks.length; j++, i++) { // traverse the interval to find the exact spot,
        if (breaks[i])
            return i;
    }

    return -1; // did not find a spot that breaks

}