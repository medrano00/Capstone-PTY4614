document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('attendanceForm');
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = new FormData(this);
        
        fetch(this.action, {
            method: this.method,
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            alert('Datos guardados con éxito!');
            // Redirigir o actualizar la página según sea necesario
        })
        .catch(error => {
            console.error('Error:', error);
            alert('Ocurrió un error al guardar los datos.');
        });
    });
});