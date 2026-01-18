#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ULTIMATE GAMINGHUB - Modern Plugin Distribution Platform
Version: 2035.1.0
Author: destroyerr1558 Advanced Code Creator
Description: Single-file Flask application with all features
"""

import json
from datetime import datetime
from flask import Flask, render_template_string, redirect, url_for, request, jsonify

# ==================== FLASK UYGULAMASI ====================
app = Flask(__name__)
app.config['SECRET_KEY'] = 'gaminghub-ultimate-2035-modern'

# ==================== TÜM VERİLER ====================
GAMES_DATA = {
    'roblox': {
        'id': 'roblox', 'name': 'Roblox', 'logo': 'https://img.icons8.com/color/96/000000/roblox.png',
        'bg_color': '#E1251B', 'description': 'Ultimate Roblox scripts and executors', 'plugins_count': 47,
        'category': 'Sandbox', 'release_year': 2006, 'trending': True
    },
    'valorant': {
        'id': 'valorant', 'name': 'Valorant', 'logo': 'https://img.icons8.com/color/96/000000/valorant.png',
        'bg_color': '#FF4655', 'description': 'Advanced aimbots and wallhacks', 'plugins_count': 32,
        'category': 'FPS', 'release_year': 2020, 'trending': True
    },
    'cs2': {
        'id': 'cs2', 'name': 'CS2', 'logo': 'https://img.icons8.com/color/96/000000/counter-strike.png',
        'bg_color': '#4B69FF', 'description': 'Professional CS2 cheats', 'plugins_count': 58,
        'category': 'FPS', 'release_year': 2023, 'trending': True
    },
    'gta5': {
        'id': 'gta5', 'name': 'GTA V', 'logo': 'https://img.icons8.com/color/96/000000/gta-5.png',
        'bg_color': '#FF7F27', 'description': 'Mod menus and money drops', 'plugins_count': 89,
        'category': 'Action', 'release_year': 2013, 'trending': True
    },
    'fortnite': {
        'id': 'fortnite', 'name': 'Fortnite', 'logo': 'https://img.icons8.com/color/96/000000/fortnite.png',
        'bg_color': '#8B5CF6', 'description': 'Aimbot and ESP enhancements', 'plugins_count': 41,
        'category': 'Battle Royale', 'release_year': 2017, 'trending': False
    },
    'minecraft': {
        'id': 'minecraft', 'name': 'Minecraft', 'logo': 'https://img.icons8.com/color/96/000000/minecraft.png',
        'bg_color': '#6CAE5B', 'description': 'Client mods and x-ray', 'plugins_count': 156,
        'category': 'Sandbox', 'release_year': 2011, 'trending': True
    },
    'overwatch2': {
        'id': 'overwatch2', 'name': 'Overwatch 2', 'logo': 'https://img.icons8.com/color/96/000000/overwatch.png',
        'bg_color': '#F99E1A', 'description': 'Hero enhancements', 'plugins_count': 28,
        'category': 'FPS', 'release_year': 2022, 'trending': False
    },
    'pubg': {
        'id': 'pubg', 'name': 'PUBG', 'logo': 'https://img.icons8.com/color/96/000000/pubg.png',
        'bg_color': '#F8A722', 'description': 'Battlefield advantages', 'plugins_count': 36,
        'category': 'Battle Royale', 'release_year': 2017, 'trending': True
    }
}

PLUGINS_DATA = {
    'roblox': [
        {'id': 1, 'name': 'Hydrogen Executor', 'desc': 'Premium script executor with built-in script hub', 
         'version': 'v4.2.1', 'author': 'Hydrogen Team', 'rating': 4.9, 'downloads': 124578, 'size': '24.7 MB',
         'updated': '2023-11-15', 'premium': True},
        {'id': 2, 'name': 'Synapse X', 'desc': 'Most advanced Roblox exploit with Lua debugger', 
         'version': 'v3.8.3', 'author': 'Synapse', 'rating': 4.8, 'downloads': 892456, 'size': '18.3 MB',
         'updated': '2023-10-28', 'premium': False},
        {'id': 3, 'name': 'Krnl', 'desc': 'Free and powerful script executor', 
         'version': 'v1.9.4', 'author': 'Krnl Team', 'rating': 4.5, 'downloads': 2456781, 'size': '15.2 MB',
         'updated': '2023-11-20', 'premium': False},
    ],
    'valorant': [
        {'id': 1, 'name': 'Valorant Ultimate Aimbot', 'desc': 'Undetectable aimbot with bone selection', 
         'version': 'v5.2.1', 'author': 'PhantomDev', 'rating': 4.9, 'downloads': 89234, 'size': '32.5 MB',
         'updated': '2023-11-16', 'premium': True},
        {'id': 2, 'name': 'ESP Pro Vision', 'desc': 'Wallhack with player information', 
         'version': 'v3.7.4', 'author': 'VisionTech', 'rating': 4.7, 'downloads': 145672, 'size': '28.3 MB',
         'updated': '2023-11-12', 'premium': False},
        {'id': 3, 'name': 'TriggerBot Deluxe', 'desc': 'Automatic shooting with custom delay', 
         'version': 'v2.9.1', 'author': 'TriggerMaster', 'rating': 4.6, 'downloads': 234567, 'size': '19.7 MB',
         'updated': '2023-11-19', 'premium': False},
    ],
    'cs2': [
        {'id': 1, 'name': 'CS2 Legit Hack', 'desc': 'Closet cheating settings for competitive', 
         'version': 'v6.1.4', 'author': 'LegitPro', 'rating': 4.9, 'downloads': 567890, 'size': '36.8 MB',
         'updated': '2023-11-20', 'premium': True},
        {'id': 2, 'name': 'SpinBot Rage', 'desc': 'Maximum rage settings for HVH', 
         'version': 'v3.2.7', 'author': 'RageTeam', 'rating': 4.8, 'downloads': 234567, 'size': '29.4 MB',
         'updated': '2023-11-15', 'premium': False},
        {'id': 3, 'name': 'Bunny Hop Assistant', 'desc': 'Perfect bhop with strafe optimizer', 
         'version': 'v2.5.1', 'author': 'MovementPro', 'rating': 4.7, 'downloads': 789012, 'size': '15.3 MB',
         'updated': '2023-11-18', 'premium': False},
    ],
    'gta5': [
        {'id': 1, 'name': 'Kiddion Mod Menu', 'desc': 'Free mod menu with money drop', 
         'version': 'v0.9.8', 'author': 'Kiddion', 'rating': 4.8, 'downloads': 3456789, 'size': '12.4 MB',
         'updated': '2023-11-14', 'premium': False},
        {'id': 2, 'name': 'Stand Ultimate', 'desc': 'Most advanced paid menu', 
         'version': 'v2.0.6', 'author': 'Stand', 'rating': 4.9, 'downloads': 456789, 'size': '45.3 MB',
         'updated': '2023-11-19', 'premium': True},
        {'id': 3, 'name': '2Take1 VIP', 'desc': 'Premium menu with Lua script support', 
         'version': 'v1.6.7', 'author': '2Take1', 'rating': 4.9, 'downloads': 234567, 'size': '52.1 MB',
         'updated': '2023-11-17', 'premium': True},
    ]
}

DOWNLOAD_URL = "https://dosya.co/pfq89dqqwr6w/plugin.exe.html"

# ==================== TÜM HTML TEMPLATE'LER ====================
def render_full_page(title, content):
    """Tam HTML sayfası oluştur"""
    return f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - GamingHub Ultimate</title>
    
    <!-- Fonts & Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {{
            --primary: #8B5CF6;
            --primary-dark: #7C3AED;
            --primary-light: #A78BFA;
            --secondary: #EC4899;
            --dark: #0F0F23;
            --darker: #0A0A1A;
            --dark-light: #1A1A2E;
            --text: #E2E8F0;
            --text-secondary: #94A3B8;
            --gradient: linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%);
            --glow: 0 0 20px rgba(139, 92, 246, 0.5);
        }}
        
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        
        body {{
            font-family: 'Poppins', sans-serif;
            background: var(--darker);
            color: var(--text);
            min-height: 100vh;
            overflow-x: hidden;
            background-image: 
                linear-gradient(rgba(139, 92, 246, 0.05) 1px, transparent 1px),
                linear-gradient(90deg, rgba(139, 92, 246, 0.05) 1px, transparent 1px);
            background-size: 50px 50px;
        }}
        
        /* Navigation */
        .navbar {{
            position: fixed;
            top: 0;
            width: 100%;
            z-index: 1000;
            background: rgba(15, 15, 35, 0.9);
            backdrop-filter: blur(10px);
            border-bottom: 1px solid rgba(139, 92, 246, 0.2);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .logo {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        
        .logo-icon {{
            width: 40px;
            height: 40px;
            background: var(--gradient);
            border-radius: 10px;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: glow 2s infinite;
        }}
        
        .logo-text {{
            font-size: 1.8rem;
            font-weight: 700;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        /* Main Content */
        .main-content {{
            margin-top: 80px;
            padding: 2rem;
            max-width: 1400px;
            margin-left: auto;
            margin-right: auto;
        }}
        
        /* Cards */
        .game-card {{
            background: rgba(26, 26, 46, 0.8);
            border-radius: 15px;
            border: 1px solid rgba(139, 92, 246, 0.2);
            transition: all 0.3s;
            overflow: hidden;
            text-decoration: none;
            display: block;
        }}
        
        .game-card:hover {{
            border-color: var(--primary);
            box-shadow: var(--glow);
            transform: translateY(-5px);
        }}
        
        .plugin-card {{
            background: rgba(26, 26, 46, 0.8);
            border-radius: 15px;
            border: 1px solid rgba(139, 92, 246, 0.2);
            transition: all 0.3s;
            padding: 1.5rem;
        }}
        
        .plugin-card:hover {{
            border-color: var(--primary);
            box-shadow: var(--glow);
            transform: translateY(-3px);
        }}
        
        /* Buttons */
        .btn-primary {{
            background: var(--gradient);
            color: white;
            padding: 0.8rem 1.5rem;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.3s;
            border: none;
            cursor: pointer;
        }}
        
        .btn-primary:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba(139, 92, 246, 0.3);
        }}
        
        /* Animations */
        @keyframes glow {{
            0%, 100% {{ box-shadow: var(--glow); }}
            50% {{ box-shadow: 0 0 30px rgba(139, 92, 246, 0.8); }}
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
        }}
        
        @keyframes slideIn {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .float {{ animation: float 3s ease-in-out infinite; }}
        .slide-in {{ animation: slideIn 0.5s ease-out; }}
        
        /* Grids */
        .games-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }}
        
        .plugins-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 1.5rem;
        }}
        
        /* Utility */
        .gradient-text {{
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        .glass-effect {{
            background: rgba(26, 26, 46, 0.6);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(139, 92, 246, 0.2);
        }}
        
        /* Footer */
        .footer {{
            background: rgba(10, 10, 26, 0.9);
            border-top: 1px solid rgba(139, 92, 246, 0.2);
            padding: 3rem 2rem;
            margin-top: 4rem;
        }}
        
        /* Responsive */
        @media (max-width: 768px) {{
            .games-grid, .plugins-grid {{
                grid-template-columns: 1fr;
            }}
            
            .navbar {{
                padding: 1rem;
                flex-direction: column;
                gap: 1rem;
            }}
            
            .main-content {{
                padding: 1rem;
                margin-top: 120px;
            }}
        }}
        
        /* Search */
        .search-box {{
            display: flex;
            position: relative;
        }}
        
        .search-input {{
            background: rgba(26, 26, 46, 0.8);
            border: 1px solid rgba(139, 92, 246, 0.3);
            border-radius: 25px 0 0 25px;
            padding: 0.5rem 1rem;
            color: var(--text);
            width: 200px;
            outline: none;
        }}
        
        .search-btn {{
            border-radius: 0 25px 25px 0;
            padding: 0.5rem 1rem;
        }}
        
        /* Stats */
        .stat-box {{
            text-align: center;
        }}
        
        .stat-number {{
            font-size: 2.5rem;
            font-weight: 700;
            background: var(--gradient);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        
        /* Hero */
        .hero-section {{
            text-align: center;
            padding: 4rem 2rem;
            margin-bottom: 4rem;
            border-radius: 20px;
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(236, 72, 153, 0.1) 100%);
            border: 1px solid rgba(139, 92, 246, 0.2);
        }}
        
        /* Game Header */
        .game-header {{
            position: relative;
            border-radius: 20px;
            overflow: hidden;
            margin-bottom: 3rem;
            height: 300px;
        }}
        
        /* Plugin Item */
        .plugin-item {{
            margin-bottom: 1.5rem;
            padding-bottom: 1.5rem;
            border-bottom: 1px solid rgba(139, 92, 246, 0.1);
        }}
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar">
        <div class="logo">
            <div class="logo-icon">
                <i class="fas fa-gamepad"></i>
            </div>
            <div class="logo-text">GamingHub</div>
        </div>
        
        <div style="display: flex; gap: 1.5rem; align-items: center;">
            <a href="/" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">
                <i class="fas fa-home"></i> Home
            </a>
            
            <form action="/search" method="get" class="search-box">
                <input type="text" name="q" placeholder="Search..." class="search-input">
                <button type="submit" class="btn-primary search-btn">
                    <i class="fas fa-search"></i>
                </button>
            </form>
        </div>
    </nav>
    
    <!-- Main Content -->
    <div class="main-content">
        {content}
    </div>
    
    <!-- Footer -->
    <footer class="footer">
        <div style="max-width: 1200px; margin: 0 auto; text-align: center;">
            <h3 class="logo-text" style="margin-bottom: 1rem;">GamingHub Ultimate</h3>
            <p style="color: var(--text-secondary); margin-bottom: 2rem;">
                The ultimate platform for gaming plugins and mods. Serving gamers worldwide since 2035.
            </p>
            <div style="color: var(--text-secondary); font-size: 0.9rem;">
                <p>© 2035 GamingHub Ultimate | Open Source Project</p>
                <p style="margin-top: 1rem; font-size: 0.8rem;">
                    <i class="fas fa-exclamation-triangle" style="color: var(--primary);"></i>
                    For educational purposes only
                </p>
            </div>
        </div>
    </footer>
    
    <script>
        // Format numbers with commas
        function formatNumber(num) {{
            return num.toString().replace(/\\B(?=(\\d{{3}})+(?!\\d))/g, ",");
        }}
        
        // Animate counting numbers
        function animateCounter(element, target) {{
            let current = 0;
            const increment = target / 50;
            
            const update = () => {{
                if (current < target) {{
                    current += increment;
                    element.textContent = formatNumber(Math.floor(current)) + '+';
                    setTimeout(update, 20);
                }} else {{
                    element.textContent = formatNumber(target) + '+';
                }}
            }};
            
            update();
        }}
        
        // Download tracking
        function trackDownload(game, plugin, name) {{
            // Send tracking request
            fetch(`/api/download/${{game}}/${{plugin}}`);
            
            // Show toast notification
            const toast = document.createElement('div');
            toast.innerHTML = `
                <div style="
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    background: linear-gradient(135deg, #8B5CF6, #EC4899);
                    color: white;
                    padding: 1rem 1.5rem;
                    border-radius: 10px;
                    z-index: 9999;
                    box-shadow: 0 5px 15px rgba(0,0,0,0.3);
                    animation: slideIn 0.3s ease-out;
                    display: flex;
                    align-items: center;
                    gap: 0.5rem;
                ">
                    <i class="fas fa-check-circle"></i>
                    <span>Downloading: ${{name}}</span>
                </div>
            `;
            document.body.appendChild(toast.firstChild);
            
            setTimeout(() => {{
                toast.remove();
            }}, 3000);
        }}
        
        // Initialize when page loads
        document.addEventListener('DOMContentLoaded', () => {{
            // Animate all stat numbers
            document.querySelectorAll('[data-count]').forEach(element => {{
                const target = parseInt(element.getAttribute('data-count'));
                animateCounter(element, target);
            }});
            
            // Add hover effects to cards
            document.querySelectorAll('.game-card, .plugin-card').forEach(card => {{
                card.addEventListener('mouseenter', () => {{
                    card.style.transform = card.classList.contains('game-card') 
                        ? 'translateY(-5px)' 
                        : 'translateY(-3px)';
                }});
                
                card.addEventListener('mouseleave', () => {{
                    card.style.transform = 'translateY(0)';
                }});
            }});
            
            // Parallax effect on mouse move
            document.addEventListener('mousemove', (e) => {{
                const cards = document.querySelectorAll('.game-card, .plugin-card');
                cards.forEach(card => {{
                    const rect = card.getBoundingClientRect();
                    const x = (e.clientX - rect.left) / rect.width;
                    const y = (e.clientY - rect.top) / rect.height;
                    
                    card.style.transform = `
                        translateY(${{card.classList.contains('game-card') ? -5 : -3}}px)
                        rotateX(${{(y - 0.5) * 2}}deg)
                        rotateY(${{(x - 0.5) * 2}}deg)
                    `;
                }});
            }});
        }});
    </script>
</body>
</html>
'''

# ==================== ROUTE'LAR ====================
@app.route('/')
def index():
    """Ana sayfa"""
    total_plugins = sum(len(plugins) for plugins in PLUGINS_DATA.values())
    total_games = len(GAMES_DATA)
    
    # Trending games
    trending_games = {k: v for k, v in GAMES_DATA.items() if v['trending']}
    
    content = f'''
    <!-- Hero Section -->
    <section class="hero-section">
        <h1 style="font-size: 3.5rem; margin-bottom: 1rem;" class="gradient-text">
            Ultimate Gaming Experience
        </h1>
        <p style="font-size: 1.2rem; color: var(--text-secondary); max-width: 600px; margin: 0 auto 2rem;">
            Access thousands of premium plugins, mods, and enhancements for your favorite games.
        </p>
        
        <div style="display: flex; justify-content: center; gap: 3rem; flex-wrap: wrap; margin-top: 3rem;">
            <div class="stat-box">
                <div data-count="{total_plugins}" class="stat-number">0</div>
                <div style="color: var(--text-secondary);">Total Plugins</div>
            </div>
            <div class="stat-box">
                <div data-count="{total_games}" class="stat-number">0</div>
                <div style="color: var(--text-secondary);">Supported Games</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">100%</div>
                <div style="color: var(--text-secondary);">Free Access</div>
            </div>
        </div>
    </section>

    <!-- Trending Games -->
    <section style="margin-bottom: 4rem;">
        <h2 style="font-size: 2rem; margin-bottom: 2rem; display: flex; align-items: center; gap: 1rem;">
            <span class="gradient-text">
                <i class="fas fa-fire"></i> Trending Games
            </span>
            <span style="font-size: 0.9rem; color: var(--text-secondary);">
                Most popular this week
            </span>
        </h2>
        
        <div class="games-grid">
    '''
    
    for game_id, game in trending_games.items():
        content += f'''
            <a href="/game/{game_id}" class="game-card">
                <div style="
                    height: 150px;
                    background: linear-gradient(135deg, {game['bg_color']}40 0%, rgba(26, 26, 46, 0.8) 100%);
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    position: relative;
                ">
                    <div style="
                        background: rgba(15, 15, 35, 0.9);
                        padding: 1rem;
                        border-radius: 10px;
                        border: 2px solid {game['bg_color']};
                    ">
                        <img src="{game['logo']}" alt="{game['name']}" style="height: 50px;">
                    </div>
                </div>
                
                <div style="padding: 1.5rem;">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                        <h3 style="color: var(--text); font-size: 1.2rem;">{game['name']}</h3>
                        <span style="
                            background: var(--gradient);
                            color: white;
                            padding: 0.3rem 0.8rem;
                            border-radius: 15px;
                            font-size: 0.8rem;
                        ">
                            {game['plugins_count']} plugins
                        </span>
                    </div>
                    
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem;">
                        {game['description']}
                    </p>
                    
                    <div style="display: flex; justify-content: space-between; font-size: 0.8rem; color: var(--text-secondary);">
                        <span><i class="fas fa-gamepad"></i> {game['category']}</span>
                        <span><i class="fas fa-calendar"></i> {game['release_year']}</span>
                    </div>
                </div>
            </a>
        '''
    
    content += '''
        </div>
    </section>

    <!-- All Games -->
    <section>
        <h2 style="font-size: 2rem; margin-bottom: 2rem; display: flex; align-items: center; gap: 1rem;">
            <span class="gradient-text">
                <i class="fas fa-th-large"></i> All Games
            </span>
            <span style="font-size: 0.9rem; color: var(--text-secondary);">
                Browse all supported titles
            </span>
        </h2>
        
        <div class="games-grid">
    '''
    
    for game_id, game in GAMES_DATA.items():
        content += f'''
            <a href="/game/{game_id}" class="game-card" style="text-align: center; padding: 1.5rem;">
                <div style="
                    width: 70px;
                    height: 70px;
                    margin: 0 auto 1rem;
                    background: linear-gradient(135deg, {game['bg_color']} 0%, rgba(26, 26, 46, 0.9) 100%);
                    border-radius: 15px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    border: 2px solid {game['bg_color']};
                ">
                    <img src="{game['logo']}" alt="{game['name']}" style="height: 40px;">
                </div>
                
                <h3 style="color: var(--text); margin-bottom: 0.5rem;">{game['name']}</h3>
                <p style="color: var(--text-secondary); font-size: 0.8rem; margin-bottom: 1rem;">
                    {game['plugins_count']} plugins
                </p>
                
                <span style="
                    display: inline-block;
                    background: rgba(139, 92, 246, 0.1);
                    color: var(--primary-light);
                    padding: 0.3rem 0.8rem;
                    border-radius: 15px;
                    font-size: 0.8rem;
                ">
                    {game['category']}
                </span>
            </a>
        '''
    
    content += '''
        </div>
    </section>

    <!-- CTA Section -->
    <section style="
        text-align: center;
        padding: 4rem 2rem;
        margin-top: 4rem;
        border-radius: 20px;
        background: linear-gradient(135deg, rgba(139, 92, 246, 0.1) 0%, rgba(236, 72, 153, 0.1) 100%);
        border: 1px solid rgba(139, 92, 246, 0.2);
    ">
        <h2 style="font-size: 2.5rem; margin-bottom: 1rem;" class="gradient-text">
            Ready to Enhance Your Game?
        </h2>
        <p style="color: var(--text-secondary); max-width: 600px; margin: 0 auto 2rem; font-size: 1.1rem;">
            Join millions of gamers. No registration required!
        </p>
        
        <a href="#games" class="btn-primary" style="padding: 1rem 2rem;">
            <i class="fas fa-rocket"></i> Browse All Plugins
        </a>
    </section>
    '''
    
    return render_template_string(render_full_page("Home", content))

@app.route('/game/<game_id>')
def game_page(game_id):
    """Oyun detay sayfası"""
    if game_id not in GAMES_DATA:
        return redirect('/')
    
    game = GAMES_DATA[game_id]
    plugins = PLUGINS_DATA.get(game_id, [])
    
    # İstatistikler
    total_downloads = sum(p['downloads'] for p in plugins) if plugins else 0
    avg_rating = round(sum(p['rating'] for p in plugins) / len(plugins), 1) if plugins else 0
    
    content = f'''
    <!-- Game Header -->
    <div class="game-header" style="background: linear-gradient(135deg, {game['bg_color']}80 0%, rgba(15, 15, 35, 0.9) 100%);">
        <div style="position: relative; z-index: 2; padding: 3rem; height: 100%; display: flex; align-items: center; gap: 3rem;">
            <div style="background: rgba(15, 15, 35, 0.9); padding: 2rem; border-radius: 15px; border: 3px solid {game['bg_color']}; box-shadow: var(--glow);">
                <img src="{game['logo']}" alt="{game['name']}" style="height: 80px;">
            </div>
            
            <div>
                <h1 style="font-size: 3rem; margin-bottom: 0.5rem; color: white;">
                    {game['name']}
                </h1>
                <p style="color: var(--text-secondary); font-size: 1.1rem; max-width: 600px;">
                    {game['description']}
                </p>
                
                <div style="display: flex; gap: 2rem; margin-top: 1.5rem;">
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 700; color: white;">
                            {game['plugins_count']}
                        </div>
                        <div style="font-size: 0.9rem; color: var(--text-secondary);">
                            Plugins
                        </div>
                    </div>
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 700; color: white;">
                            {total_downloads:,}
                        </div>
                        <div style="font-size: 0.9rem; color: var(--text-secondary);">
                            Downloads
                        </div>
                    </div>
                    <div>
                        <div style="font-size: 1.5rem; font-weight: 700; color: white;">
                            {avg_rating}/5.0
                        </div>
                        <div style="font-size: 0.9rem; color: var(--text-secondary);">
                            Avg Rating
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Plugins -->
    <div>
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
            <h2 style="font-size: 2rem; display: flex; align-items: center; gap: 1rem;">
                <span class="gradient-text">
                    <i class="fas fa-cubes"></i> Available Plugins
                </span>
                <span style="font-size: 0.9rem; color: var(--text-secondary);">
                    {len(plugins)} plugins
                </span>
            </h2>
        </div>
        
        <div class="plugins-grid">
    '''
    
    for plugin in plugins:
        stars = ''.join(['<i class="fas fa-star" style="color: #F59E0B;"></i>' if i < int(plugin['rating']) 
                        else '<i class="far fa-star" style="color: #4B5563;"></i>' for i in range(5)])
        
        premium_badge = '''
        <span style="background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%); color: white; 
               padding: 0.2rem 0.8rem; border-radius: 15px; font-size: 0.7rem;">
            PREMIUM
        </span>''' if plugin['premium'] else '''
        <span style="background: linear-gradient(135deg, #10B981 0%, #059669 100%); color: white; 
               padding: 0.2rem 0.8rem; border-radius: 15px; font-size: 0.7rem;">
            FREE
        </span>'''
        
        content += f'''
            <div class="plugin-card">
                <div style="display: flex; gap: 1rem; margin-bottom: 1rem;">
                    <div style="width: 50px; height: 50px; background: linear-gradient(135deg, {game['bg_color']} 0%, rgba(26, 26, 46, 0.9) 100%); 
                         border-radius: 10px; display: flex; align-items: center; justify-content: center; border: 2px solid {game['bg_color']};">
                        <i class="fas fa-puzzle-piece" style="color: white; font-size: 1.2rem;"></i>
                    </div>
                    
                    <div style="flex: 1;">
                        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                            <h3 style="color: var(--text); font-size: 1.2rem;">{plugin['name']}</h3>
                            {premium_badge}
                        </div>
                        
                        <div style="display: flex; gap: 1rem; font-size: 0.85rem; color: var(--text-secondary); margin-top: 0.5rem;">
                            <span><i class="fas fa-user"></i> {plugin['author']}</span>
                            <span><i class="fas fa-code-branch"></i> {plugin['version']}</span>
                        </div>
                    </div>
                </div>
                
                <p style="color: var(--text-secondary); font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.5;">
                    {plugin['desc']}
                </p>
                
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
                    <div style="display: flex; align-items: center; gap: 0.5rem;">
                        <div style="display: flex; gap: 0.2rem;">
                            {stars}
                        </div>
                        <span style="color: var(--text-secondary); font-size: 0.9rem;">
                            {plugin['rating']}/5.0
                        </span>
                    </div>
                    
                    <div style="color: var(--text-secondary); font-size: 0.9rem;">
                        <i class="fas fa-download"></i> {plugin['downloads']:,}
                    </div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="color: var(--text-secondary); font-size: 0.8rem;">
                        <i class="fas fa-hdd"></i> {plugin['size']}
                    </div>
                    
                    <a href="{DOWNLOAD_URL}" 
                       class="btn-primary" 
                       onclick="trackDownload('{game_id}', '{plugin['id']}', '{plugin['name']}')"
                       style="padding: 0.8rem 1.5rem;">
                        <i class="fas fa-download"></i> Download Now
                    </a>
                </div>
            </div>
        '''
    
    content += f'''
        </div>
    </div>

    <!-- Download Info -->
    <div style="margin-top: 3rem; padding: 2rem; background: rgba(139, 92, 246, 0.05); 
         border-radius: 15px; border: 1px solid rgba(139, 92, 246, 0.2);">
        <h3 style="font-size: 1.5rem; margin-bottom: 1rem; display: flex; align-items: center; gap: 1rem;">
            <i class="fas fa-info-circle" style="color: var(--primary);"></i>
            Download Instructions
        </h3>
        
        <div style="color: var(--text-secondary); line-height: 1.6;">
            <p>1. Click "Download Now" button to be redirected to download page.</p>
            <p>2. All plugins are distributed via: <code style="background: rgba(139, 92, 246, 0.1); padding: 0.2rem 0.5rem; border-radius: 4px; color: var(--primary-light);">{DOWNLOAD_URL}</code></p>
            <p>3. Extract files and follow included instructions.</p>
            <p>4. For safety, test in controlled environment first.</p>
        </div>
    </div>
    '''
    
    return render_template_string(render_full_page(game['name'], content))

@app.route('/search')
def search():
    """Arama sayfası"""
    query = request.args.get('q', '').lower()
    results = []
    
    if query:
        # Oyunlarda ara
        for game_id, game in GAMES_DATA.items():
            if query in game['name'].lower() or query in game['description'].lower():
                results.append({
                    'type': 'game',
                    'id': game_id,
                    'name': game['name'],
                    'description': game['description'],
                    'color': game['bg_color']
                })
        
        # Pluginlerde ara
        for game_id, plugins in PLUGINS_DATA.items():
            for plugin in plugins:
                if query in plugin['name'].lower() or query in plugin['desc'].lower():
                    results.append({
                        'type': 'plugin',
                        'id': plugin['id'],
                        'game_id': game_id,
                        'name': plugin['name'],
                        'description': plugin['desc'],
                        'rating': plugin['rating'],
                        'color': GAMES_DATA[game_id]['bg_color']
                    })
    
    content = f'''
    <!-- Search Header -->
    <div style="text-align: center; margin-bottom: 3rem;">
        <h1 style="font-size: 2.5rem; margin-bottom: 1rem;" class="gradient-text">
            <i class="fas fa-search"></i> Search Results
        </h1>
        
        <form action="/search" method="get" style="max-width: 600px; margin: 0 auto; position: relative;">
            <input type="text" name="q" value="{query}" placeholder="Search games, plugins..." style="
                width: 100%;
                background: rgba(26, 26, 46, 0.8);
                border: 2px solid var(--primary);
                border-radius: 50px;
                padding: 1rem 1.5rem;
                color: var(--text);
                font-size: 1rem;
                outline: none;
            ">
            <button type="submit" class="btn-primary" style="
                position: absolute;
                right: 10px;
                top: 50%;
                transform: translateY(-50%);
                padding: 0.8rem;
                border-radius: 50%;
            ">
                <i class="fas fa-search"></i>
            </button>
        </form>
        
        {f'<p style="color: var(--text-secondary); margin-top: 1rem;">Found <strong style="color: var(--primary-light);">{len(results)}</strong> results for "{query}"</p>' if query else ''}
    </div>
    '''
    
    if query:
        if results:
            content += '''
            <div class="plugins-grid">
            '''
            
            for result in results:
                icon = 'fa-gamepad' if result['type'] == 'game' else 'fa-puzzle-piece'
                badge = 'Game' if result['type'] == 'game' else 'Plugin'
                link = f'/game/{result["id"]}' if result['type'] == 'game' else f'/game/{result["game_id"]}'
                
                content += f'''
                <div class="plugin-card">
                    <div style="display: flex; align-items: center; gap: 1rem; margin-bottom: 1rem;">
                        <div style="width: 50px; height: 50px; background: linear-gradient(135deg, {result['color']} 0%, rgba(26, 26, 46, 0.9) 100%); 
                             border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                            <i class="fas {icon}" style="color: white; font-size: 1.2rem;"></i>
                        </div>
                        
                        <div style="flex: 1;">
                            <h3 style="color: var(--text); font-size: 1.2rem;">{result['name']}</h3>
                            <div style="display: flex; align-items: center; gap: 1rem; margin-top: 0.5rem;">
                                <span style="background: rgba(139, 92, 246, 0.1); color: var(--primary-light); 
                                       padding: 0.2rem 0.8rem; border-radius: 15px; font-size: 0.8rem;">
                                    {badge}
                                </span>
                                
                                {f'<span style="color: var(--text-secondary); font-size: 0.85rem;"><i class="fas fa-star" style="color: #F59E0B;"></i> {result["rating"]}</span>' if result['type'] == 'plugin' else ''}
                            </div>
                        </div>
                    </div>
                    
                    <p style="color: var(--text-secondary); font-size: 0.9rem; margin-bottom: 1rem; line-height: 1.5;">
                        {result['description']}
                    </p>
                    
                    <div style="text-align: right;">
                        <a href="{link}" class="btn-primary" style="padding: 0.5rem 1rem; font-size: 0.9rem;">
                            View Details <i class="fas fa-arrow-right"></i>
                        </a>
                    </div>
                </div>
                '''
            
            content += '''
            </div>
            '''
        else:
            content += '''
            <div style="text-align: center; padding: 4rem 2rem;">
                <i class="fas fa-search" style="font-size: 4rem; color: var(--text-secondary); margin-bottom: 1rem;"></i>
                <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: var(--text);">
                    No results found
                </h3>
                <p style="color: var(--text-secondary); max-width: 400px; margin: 0 auto;">
                    Try different search terms or browse all games.
                </p>
            </div>
            '''
    
    return render_template_string(render_full_page("Search", content))

@app.route('/download/<game_id>/<int:plugin_id>')
def download_plugin(game_id, plugin_id):
    """Plugin indirme - Direkt yönlendirme"""
    # İndirme istatistiğini artır
    if game_id in PLUGINS_DATA:
        for plugin in PLUGINS_DATA[game_id]:
            if plugin['id'] == plugin_id:
                plugin['downloads'] += 100
                break
    
    # Direkt indirme linkine yönlendir
    return redirect(DOWNLOAD_URL)

@app.route('/api/download/<game_id>/<int:plugin_id>')
def api_download(game_id, plugin_id):
    """API indirme endpoint'i"""
    # İndirme istatistiğini artır
    if game_id in PLUGINS_DATA:
        for plugin in PLUGINS_DATA[game_id]:
            if plugin['id'] == plugin_id:
                plugin['downloads'] += 1
                break
    
    return jsonify({'status': 'success', 'download_url': DOWNLOAD_URL})

@app.route('/api/stats')
def api_stats():
    """Genel istatistikler API"""
    total_downloads = 0
    total_plugins = 0
    
    for game_id in PLUGINS_DATA:
        for plugin in PLUGINS_DATA[game_id]:
            total_downloads += plugin['downloads']
            total_plugins += 1
    
    return jsonify({
        'total_games': len(GAMES_DATA),
        'total_plugins': total_plugins,
        'total_downloads': total_downloads,
        'avg_rating': 4.7,
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/games')
def api_games():
    """Tüm oyunlar API"""
    return jsonify(GAMES_DATA)

@app.route('/api/plugins/<game_id>')
def api_plugins(game_id):
    """Oyun pluginleri API"""
    return jsonify(PLUGINS_DATA.get(game_id, []))

@app.errorhandler(404)
def page_not_found(e):
    """404 sayfası"""
    content = '''
    <div style="text-align: center; padding: 6rem 2rem;">
        <i class="fas fa-exclamation-triangle" style="font-size: 5rem; color: var(--primary); margin-bottom: 2rem;"></i>
        <h1 style="font-size: 3rem; margin-bottom: 1rem;" class="gradient-text">404</h1>
        <p style="font-size: 1.2rem; color: var(--text-secondary); margin-bottom: 2rem;">
            The page you're looking for doesn't exist.
        </p>
        <a href="/" class="btn-primary">
            <i class="fas fa-home"></i> Back to Home
        </a>
    </div>
    '''
    return render_template_string(render_full_page("404 Not Found", content)), 404

# ==================== ANA FONKSİYON ====================
if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 ULTIMATE GAMINGHUB - Modern Plugin Distribution Platform")
    print("="*70)
    print(f"📁 Total Games: {len(GAMES_DATA)}")
    print(f"📦 Total Plugins: {sum(len(plugins) for plugins in PLUGINS_DATA.values())}")
    print(f"🎨 Theme: Ultra Modern Purple Dark")
    print(f"🌐 Language: English Only")
    print(f"🔗 Download URL: {DOWNLOAD_URL}")
    print("="*70)
    print("\n✅ Server is running on: http://localhost:5000")
    print("   Press CTRL+C to stop\n")
    
    # Flask'ı debug modda başlat
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)
