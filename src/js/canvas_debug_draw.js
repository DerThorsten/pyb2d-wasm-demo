
class CanvasDebugDraw {
    constructor(canvas) {
        this.canvas = canvas;
        this.context = canvas.getContext("2d")
    }


    draw_circle_impl(center, radius, color, axis){
        this.context.beginPath()
        this.context.arc(center[0], center[1], radius, 0, 2 * Math.PI, false)
        
        if(axis !== undefined)
        {
            this.context.fillStyle = `rgb(${color[0]},${color[1]},${color[2]})`
            this.context.fill()
        }
        else
        {
            this.context.strokeStyle = `rgb(${color[0]},${color[1]},${color[2]})`
            this.context.lineWidth = 1
            this.context.stroke()
        }
    }

    draw_segment_impl(points, color){
        this.context.beginPath();
        this.context.moveTo(points[0],points[1]);
        this.context.lineTo(points[2],points[3]);
        this.context.strokeStyle = `rgb(${color[0]},${color[1]},${color[2]})`;
        this.context.lineWidth = 1
        this.context.stroke()
    }

    draw_segment(p1,p2, color, lineWidth=1){
        this.context.beginPath();
        this.context.moveTo(p1[0],p1[1]);
        this.context.lineTo(p2[0],p2[1]);
        this.context.strokeStyle = `rgb(${color[0]},${color[1]},${color[2]})`;
        this.context.lineWidth = lineWidth
        this.context.stroke()
    }

    draw_poly_impl(polygon_length, polygon_points, color, solid, lineWidth=1){
        this.context.beginPath();

        this.context.moveTo(polygon_points[0],polygon_points[1]);
        for(let i=1; i<polygon_length; i++)
        {
            this.context.lineTo(polygon_points[2*i],polygon_points[2*i+1]);
        }
        this.context.lineTo(polygon_points[0],polygon_points[1]);
        this.context.closePath();
        if(solid)
        {
            this.context.fillStyle = `rgb(${color[0]},${color[1]},${color[2]})`;
            this.context.fill()
        }
        else
        {
            this.context.strokeStyle = `rgb(${color[0]},${color[1]},${color[2]})`;
            this.lineWidth = lineWidth
            this.context.stroke()
        }
    }


    draw_polygons(points, sizes, colors, solid){

        const n = sizes.length
        var offset = 0
        for (let i = 0; i < n; i++) {
            const polygon_length = sizes[i];
            const polygon_points = points.subarray(offset, 2*polygon_length)
            const polygon_color = colors.subarray(i*3, i*3 +3)
            this.draw_poly_impl(polygon_length,polygon_points,polygon_color, solid)
            offset += 2 * polygon_length;
        }
    }


    draw_solid_circles(centers, radii, axis, colors){
        const n = radii.length
        for (let i = 0; i < n; i++) {
            const center = centers.subarray(2*i, 2*i+2)
            const radius = radii[i]
            const color = colors.subarray(3*i, 3*i+3)
            const ax = axis.subarray(2*i, 2*i+2)
            this.draw_circle_impl(center, radius, color, ax)
        }
    }
    draw_circles(centers, radii, colors){
        const n = radii.length
        for (let i = 0; i < n; i++) {
            const center = centers.subarray(2*i, 2*i+2)
            const radius = radii[i]
            const color = colors.subarray(3*i, 3*i+3)
            this.draw_circle_impl(center, radius, color, undefined)
        }
    }
    draw_segments(points, colors){
        const n = points.length / 4
        for (let i = 0; i < n; i++) {
            const p = points.subarray(4*i, 4*i+4)
            const color = colors.subarray(3*i, 3*i+3)
            this.draw_segment_impl(p, color)
        }
    }
}

export {CanvasDebugDraw}