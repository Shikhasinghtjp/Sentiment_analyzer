    // Toggle dark mode
        function toggleDarkMode() {
            document.body.classList.toggle('dark-mode');
        }

        // Toast animation
        const toast = document.getElementById('toast');
        if (toast) {
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 4000);
        }

        // Lottie animation
        bodymovin.loadAnimation({
            container: document.getElementById('animation'),
            renderer: 'svg',
            loop: true,
            autoplay: true,
            path: 'https://lottie.host/f4ed1f64-52ac-4e36-931f-6b6249f1c67e/ypdOtKHWDN.json'
        });