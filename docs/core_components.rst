Brain Simulation Ecosystem Core Component 
=========================================
.. raw:: html

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Brain Simulation Ecosystem</title>  

        <style>
            /* 基础重置和全局样式 */
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            
            body {
                font-family: 'Segoe UI', 'Roboto', 'Helvetica Neue', Arial, sans-serif;
                line-height: 1.6;
                color: #2c3e50;
                background: #f8f9fa;
                max-width: 100%;
                overflow-x: hidden;
                transition: background-color 0.3s ease, color 0.3s ease;
            }
            
            /* 暗色主题 */
            html[data-theme="dark"] body {
                background: #121212;
                color: #e0e0e0;
            }
            
            .container1 {
                width: 100%;
                max-width: 1400px;
                margin: 0 auto;
                display: grid;       /* 使用网格布局 */
                grid: auto-flow / 1fr .2fr;     /* 自动行高，列比例为5:1 */
                gap: 20px;           /* 网格间隙 */
                align-items: center; /* 垂直居中 */
                margin-bottom: 10px;
                padding: 0 20px;
            }
             .container {
                width: 100%;
                max-width: 1400px;
                margin: 0 auto;
                padding: 0 20px;
            }
            
            /* 头部样式 */
            .hero {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 25%, #4d6ac1 50%, #2a4a7f 75%, #0f2e5c 100%);
                padding: 3rem 0;
                text-align: center;
                position: relative;
                overflow: hidden;
                margin: 0 auto 1rem;
                width: 100%;
                max-width: 1400px;
                transition: background 0.3s ease;
                border: none;
                box-shadow: none;
                border-radius: 24px;
                box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.6);
                background-size: cover;
            }
            
            html[data-theme="dark"] .hero {
                background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            }
            
            .hero::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                bottom: 0;
                background: 
                    radial-gradient(circle at 20% 80%, rgba(255,255,255,0.1) 0%, transparent 20%),
                    radial-gradient(circle at 80% 20%, rgba(255,255,255,0.1) 0%, transparent 20%);
            }
            
            html[data-theme="dark"] .hero::before {
                background: 
                    radial-gradient(circle at 20% 80%, rgba(0,0,0,0.2) 0%, transparent 20%),
                    radial-gradient(circle at 80% 20%, rgba(0,0,0,0.2) 0%, transparent 20%);
            }
            
            .hero-content {
                position: relative;
                z-index: 2;
                width: 100%;
                text-align: left; /* 改为左对齐 */
                display: flex;
                flex-direction: column;
                padding-inline: 100px;
            }
            
            .hero h1 {
                font-size: 3.5rem;
                margin-bottom: 1rem;
                font-weight: 700;
                color: white;
                transition: color 0.3s ease;
            }
            
            html[data-theme="dark"] .hero h1 {
                color: white;
            }
            
            .hero p {
                font-size: 1.4rem;
                max-width: 800px;
                margin: 0 auto 2rem;
                opacity: 0.9;
                color: #bdc1c6;
                transition: color 0.3s ease;
            }
            
            html[data-theme="dark"] .hero p {
                color: #e0e0e0;
            }
            
            .cta-button {
                display: inline-block;
                background: #1A73E8;
                color:#ffffff !important;
                padding: 1rem 2rem;
                border-radius: 5px;
                text-decoration: none;
                font-weight: 600;
                transition: all 0.3s ease;
                box-shadow: 0 4px 15px rgba(0, 188, 212, 0.3);
                align-self: flex-start;
                width: max-content; 
            }
            html[data-theme="dark"] .cta-button {
                background: #8ab4f8;
                color: #e0e0e0;
            }
            
            .cta-button:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 20px rgba(0, 188, 212, 0.4);
            }
            
            /* 主要内容区域 */
            .main-content {
                padding: 2rem 0;
            }
            
            .section-title {
                text-align: center;
                margin-bottom: 3rem;
                font-size: 2.2rem;
                color: #0a1172;
                position: relative;
                padding-bottom: 15px;
                transition: color 0.3s ease;
            }
            
            html[data-theme="dark"] .section-title {
                color: #8ab4f8;
            }
            
            .section-title::after {
                content: '';
                position: absolute;
                bottom: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 80px;
                height: 4px;
                background: #03a9f4;
                border-radius: 2px;
            }
            
            html[data-theme="dark"] .section-title::after {
                background: #8ab4f8;
            }
            
            /* 卡片网格布局 */
            .card-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(min(100%, 350px), 1fr));
                gap: 2rem;
                margin-bottom: 4rem;
            }

            .card-grid:has(.card:nth-child(1):last-child) {
                grid-template-columns: repeat(auto-fit, minmax(min(100%, 350px), 1fr));
                max-width: 430px;
            }

            
            .card {
                background: white;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
                transition: all 0.3s ease;
                height: 100%;
                display: flex;
                flex-direction: column;
            }
            
            html[data-theme="dark"] .card {
                background: #1e1e1e;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            }
            
            .card:hover {
                transform: translateY(-10px);
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.12);
            }
            
            html[data-theme="dark"] .card:hover {
                box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
            }
            
            .card-image {
                height: 180px;
                overflow: hidden;
                display: flex;
                align-items: center;
                justify-content: center;
                background: #f4f7fe;
                padding: 1rem;
                transition: background 0.3s ease;
            }
            
            html[data-theme="dark"] .card-image {
                background: #2d2d2d;
            }
            
            .card-image img {
                max-height: 140px;
                max-width: 100%;
                object-fit: contain;
            }
            
            .card-content {
                padding: 1.5rem;
                flex-grow: 1;
                display: flex;
                flex-direction: column;
            }
            
            .card-title {
                font-size: 1.5rem;
                margin-bottom: 1rem;
                margin-top: 1rem;
                color: #0a1172;
                transition: color 0.3s ease;
            }
            
            html[data-theme="dark"] .card-title {
                color: #8ab4f8;
            }
            
            .card-description {
                margin-bottom: 1.5rem;
                flex-grow: 1;
                color: #555;
                transition: color 0.3s ease;
            }
            
            html[data-theme="dark"] .card-description {
                color: #bdc1c6;
            }
            
            .card-link {
                display: inline-block;
                color: #03a9f4;
                text-decoration: none;
                font-weight: 600;
                align-self: flex-start;
                position: relative;
                padding-right: 20px;
                transition: color 0.3s ease;
                font-size: clamp(0.9rem, 2vw, 1rem);
            }
            
            html[data-theme="dark"] .card-link {
                color: #8ab4f8;
            }
            
            .card-link::after {
                content: '→';
                position: absolute;
                right: 0;
                top: 50%;
                transform: translateY(-50%);
                transition: transform 0.3s ease;
            }
            
            .card-link:hover::after {
                transform: translate(5px, -50%);
            }
            
            /* 安装部分 */
            .install-section {
                background: white;
                border-radius: 12px;
                padding: 2.5rem;
                margin-bottom: 4rem;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
                transition: all 0.3s ease;
            }
            
            html[data-theme="dark"] .install-section {
                background: #1e1e1e;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            }
            
            .tabs {
                display: flex;
                border-bottom: 2px solid #eaeaea;
                margin-bottom: 1.5rem;
                transition: border-color 0.3s ease;
            }
            
            html[data-theme="dark"] .tabs {
                border-bottom: 2px solid #333;
            }
            
            .tab {
                padding: 1rem 1.5rem;
                background: #f8f9fa;
                margin-right: 5px;
                border-radius: 5px 5px 0 0;
                cursor: pointer;
                transition: all 0.3s ease;
            }
            
            html[data-theme="dark"] .tab {
                background: #2d2d2d;
                color: #e0e0e0;
            }
            
            .tab.active {
                background: #03a9f4;
                color: white;
            }
            
            html[data-theme="dark"] .tab.active {
                background: #8ab4f8;
                color: #121212;
            }
            
            .code-block {
                background: #2c3e50;
                color: #ecf0f1;
                padding: 1.5rem;
                border-radius: 8px;
                overflow-x: auto;
                font-family: 'Fira Code', 'Monaco', 'Consolas', monospace;
                margin: 1rem 0;
            }
            
            html[data-theme="dark"] .footer {
                background:linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
            }
            
           
            
            
            html[data-theme="dark"] .footer a {
                color: #8ab4f8;
            }
            
            /* 主题切换按钮 */
            .theme-toggle {
                position: fixed;
                top: 20px;
                right: 20px;
                background: #f8f9fa;
                border: none;
                border-radius: 50%;
                width: 50px;
                height: 50px;
                cursor: pointer;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
                z-index: 1000;
                transition: all 0.3s ease;
            }
            
            html[data-theme="dark"] .theme-toggle {
                background: #2d2d2d;
                color: #f8f9fa;
            }
            
            /* 响应式设计 */
            @media (max-width: 1240px) {
                .hero h1 {
                    font-size: 42px;
                    margin-bottom: 24px;
                }
            }

            @media (max-width: 1020px) {
                .hero h1 {
                    font-size: 32px;
                }
            }

            @media (max-width: 860px) {
                .card-grid {
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                }
            }

            @media (max-width: 800px) {
                .hero {
                    width: 80%;
                    padding: 2rem 0;
                }
                
                .hero h1 {
                    font-size: 28px;
                }
                
                .hero p {
                    font-size: 1.1rem;
                }
            }
        </style>
    </head>
    <body>
        <!-- 主题切换按钮 -->
        <button class="theme-toggle" id="themeToggle">🌙</button>




        <!----------------------------网页文字内容 ---------------------------------------------->
        <header class="hero">
            <div class="container1">
                <div class="hero-content">
                    <h1>Brain simulation ecosystem</h1>
                    <p>Advanced tools for brain dynamics modeling, simulation, and analysis.</p>
                    <a href="./getting_started.html" class="cta-button">Get Started</a>
                </div>
                <img src="./_static/bdp-ecosystem.png" class="hero-image">
            </div>
        </header>

        <main class="main-content">
            <div class="container">
                <h2 class="section-title">Differentiable brain modeling</h2>
                
                <div class="card-grid">
                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/brainpy/BrainPy/master/images/logo.png" alt="BrainPy Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainPy</h3>
                            <p class="card-description">Legacy framework for brain dynamics programming with high flexibility and performance.</p>
                            <a href="https://brainpy.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/chaobrain/brainstate/main/docs/_static/brainstate.png" alt="BrainState Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainState</h3>
                            <p class="card-description">Modeling of point-based spiking neural networks.</p>
                            <a href="https://brainstate.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/chaobrain/braincell/main/docs/_static/braincell.png" alt="BrainCell Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainCell</h3>
                            <p class="card-description">Modeling of biologically detailed Hodgkin–Huxley neurons and networks.</p>
                            <a href="https://braincell.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-image">
                            <img src="./_static/brainmass.png" alt="BrainMass Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainMass</h3>
                            <p class="card-description">Whole-brain modeling with differentiable neural mass models.</p>
                            <a href="https://brainmass.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="container">
                <h2 class="section-title">Infrastructure</h2>
                
                <div class="card-grid">
                    
                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/chaobrain/braintaichi/main/docs/_static/braintaichi.png" alt="BrainTaichi Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainTaichi</h3>
                            <p class="card-description">Event-driven operator customization based on Taichi Lang.</p>
                            <a href="https://braintaichi.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>
                    
                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/chaobrain/saiunit/main/docs/_static/brainunit.png" alt="BrainUnit Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainUnit</h3>
                            <p class="card-description">Physical units and unit-aware mathematical system for brain modeling.</p>
                            <a href="https://brainunit.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-image">
                            <img src="./_static/brainevent.png" alt="BrainEvent Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainEvent</h3>
                            <p class="card-description">Event-driven algorithms and data structures for brain dynamics.</p>
                            <a href="https://brainevent.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/chaobrain/brainscale/main/docs/_static/brainscale.jpg" alt="BrainScale Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainScale</h3>
                            <p class="card-description">Online learnng system for large-scale brain models.</p>
                            <a href="https://brainscale.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>

                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/chaobrain/braintools/main/docs/_static/braintools.jpg" alt="BrainTools Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainTools</h3>
                            <p class="card-description">Modeling tools for general-purpose brain simulation.</p>
                            <a href="https://braintools.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div>
                </div> 
            </div>  

            <div class="container">
                <h2 class="section-title">Compilation</h2>
                
                <div class="card-grid">
                    <div class="card">
                        <div class="card-image">
                            <img src="https://raw.githubusercontent.com/chaobrain/brainstate/main/docs/_static/brainstate.png" alt="BrainState Logo">
                        </div>
                        <div class="card-content">
                            <h3 class="card-title">BrainState</h3>
                            <p class="card-description">State-based IR compilation for brain models.</p>
                            <a href="https://brainstate.readthedocs.io/" class="card-link">Learn More</a>
                        </div>
                    </div> 
                </div>  
             
                
                <section id="install" class="install-section">
                        <h2 class="section-title">Installation</h2>
                        
                        <div class="tabs">
                            <div class="tab active" onclick="switchTab(event, 'cpu')">CPU</div>
                            <div class="tab" onclick="switchTab(event, 'gpu')">GPU (CUDA 12.0)</div>
                            <div class="tab" onclick="switchTab(event, 'tpu')">TPU</div>
                        </div>
                        
                        <div id="cpu" class="tab-content active">
                            <div class="code-block">
                                pip install BrainX[cpu] -U
                            </div>
                        </div>
                        
                        <div id="gpu" class="tab-content" style="display:none;">
                            <div class="code-block">
                                pip install BrainX[cuda12] -U
                            </div>
                        </div>
                        
                        <div id="tpu" class="tab-content" style="display:none;">
                            <div class="code-block">
                                pip install BrainX[tpu] -U
                            </div>
                        </div>
                    </section>
            </div>           
        </main>
        
        
        <script>
            function switchTab(event, tabId) {
                // 隐藏所有标签内容
                document.querySelectorAll('.tab-content').forEach(tab => {
                    tab.style.display = 'none';
                });
                
                // 移除所有标签的活动类
                document.querySelectorAll('.tab').forEach(tab => {
                    tab.classList.remove('active');
                });
                
                // 显示选中的标签内容
                document.getElementById(tabId).style.display = 'block';
                
                // 为选中的标签添加活动类
                event.currentTarget.classList.add('active');
            }

            // 主题切换功能
            const themeToggle = document.getElementById('themeToggle');
            const html = document.documentElement;
            
            // 检查本地存储或系统偏好
            const savedTheme = localStorage.getItem('theme');
            const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
            
            if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
                html.setAttribute('data-theme', 'dark');
                themeToggle.textContent = '☀️';
            } else {
                html.removeAttribute('data-theme');
                themeToggle.textContent = '🌙';
            }
            
            // 切换主题
            themeToggle.addEventListener('click', () => {
                if (html.getAttribute('data-theme') === 'dark') {
                    html.removeAttribute('data-theme');
                    localStorage.setItem('theme', 'light');
                    themeToggle.textContent = '🌙';
                } else {
                    html.setAttribute('data-theme', 'dark');
                    localStorage.setItem('theme', 'dark');
                    themeToggle.textContent = '☀️';
                }
            });
        </script>
    </body>
    </html>