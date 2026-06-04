function criarGrafico(canvasId, labels, values) {

    const ctx = document.getElementById(canvasId);

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Valores',
                data: values
            }]
        }
    });
}
