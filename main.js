document.addEventListener('DOMContentLoaded', () => {
    // --- CUSTOM CURSOR LOGIC ---
    const cursorDot = document.querySelector('[data-cursor-dot]');
    const cursorOutline = document.querySelector('[data-cursor-outline]');

    window.addEventListener("mousemove", function (e) {
        const posX = e.clientX;
        const posY = e.clientY;

        // Dot follows instantly
        if (cursorDot) {
            cursorDot.style.left = `${posX}px`;
            cursorDot.style.top = `${posY}px`;
        }

        // Outline follows with subtle delay/animation (handled by CSS transition, we just set pos)
        if (cursorOutline) {
            cursorOutline.animate({
                left: `${posX}px`,
                top: `${posY}px`
            }, { duration: 500, fill: "forwards" });
        }
    });

    // Hover effect for links/tiles
    const interactiveElements = document.querySelectorAll('a, button, .tile, .project-card');
    interactiveElements.forEach(el => {
        el.addEventListener('mouseenter', () => {
            if (cursorOutline) {
                cursorOutline.style.transform = 'translate(-50%, -50%) scale(1.2)'; // Subtle scale
                cursorOutline.style.borderColor = 'var(--text-main)';
                cursorOutline.style.backgroundColor = 'rgba(255, 255, 255, 0.05)';
            }
        });
        el.addEventListener('mouseleave', () => {
            if (cursorOutline) {
                cursorOutline.style.transform = 'translate(-50%, -50%) scale(1)';
                cursorOutline.style.borderColor = 'rgba(255, 255, 255, 0.3)';
                cursorOutline.style.backgroundColor = 'transparent';
            }
        });
    });

    // --- 3D TILT EFFECT ---
    const allTiles = document.querySelectorAll('.tile'); // All tiles for tilt effect

    allTiles.forEach(tile => {
        tile.addEventListener('mousemove', (e) => {
            if (tile.classList.contains('expanded')) return; // No tilt if expanded

            const rect = tile.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            // Calculate rotation based on mouse position
            const xPct = x / rect.width;
            const yPct = y / rect.height;

            // --- UPDATE SPOTLIGHT VARIABLES ---
            tile.style.setProperty('--mouse-x', `${x}px`);
            tile.style.setProperty('--mouse-y', `${y}px`);

            const xRotation = (yPct - 0.5) * 20 * -1; // -1 to invert natural tilt
            const yRotation = (xPct - 0.5) * 20;

            tile.style.transform = `perspective(1000px) rotateX(${xRotation}deg) rotateY(${yRotation}deg) scale(1.02)`;
        });

        tile.addEventListener('mouseleave', () => {
            if (tile.classList.contains('expanded')) return;
            tile.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale(1)';
        });
    });

    const expandableTiles = document.querySelectorAll('.tile[data-expandable="true"]'); // Only expandable tiles for expansion logic
    const body = document.body;
    let activeTile = null;

    // --- EXPANSION LOGIC ---
    expandableTiles.forEach(tile => {
        tile.addEventListener('click', (e) => {
            // If already active, do nothing (click close btn to close)
            if (tile.classList.contains('expanded')) return;

            // If another tile is active, close it first
            if (activeTile) {
                closeTile(activeTile);
            }

            openTile(tile);
        });

        // Handle Close Button inside the tile
        const closeBtn = tile.querySelector('.close-btn');
        if (closeBtn) {
            closeBtn.addEventListener('click', (e) => {
                e.stopPropagation(); // Prevent tile click event
                closeTile(tile);
            });
        }
    });

    // Close on ESC key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && activeTile) {
            closeTile(activeTile);
        }
    });

    function openTile(tile) {
        // Reset tilt transform
        tile.style.transform = 'none';

        // Save current position for animation logic if we were using advanced FLIP, 
        // but for now simple class toggle 
        tile.classList.add('expanded');
        body.classList.add('has-expanded-tile');

        // Show Full Content
        const fullContent = tile.querySelector('.full-content');
        if (fullContent) fullContent.classList.remove('hidden');

        // Hide Preview items if they clutter (optional)
        // tile.querySelector('.content.preview').style.opacity = '0';

        activeTile = tile;
    }

    function closeTile(tile) {
        tile.classList.remove('expanded');
        body.classList.remove('has-expanded-tile');

        // Hide Full Content
        const fullContent = tile.querySelector('.full-content');
        setTimeout(() => {
            if (fullContent) fullContent.classList.add('hidden');
        }, 300); // Wait for transition if needed

        activeTile = null;
    }

    // --- MODAL DATA & LOGIC ---
    const projectData = {
        "shift": {
            title: "Shift Manager App",
            desc: "A comprehensive control panel for managing employee shifts. Built with Python and Flet, it features a drag-and-drop interface, automatic PDF generation, and Google Calendar integration. It allows managers to organize weekly schedules with conflict detection and export them instantly.",
            stack: ["Python", "Flet", "Android", "Google API", "PDF Generation"],
            icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect><line x1="16" y1="2" x2="16" y2="6"></line><line x1="8" y1="2" x2="8" y2="6"></line><line x1="3" y1="10" x2="21" y2="10"></line></svg>',
            link: "#"
        },
        "data": {
            title: "Health Data Analysis",
            desc: "An in-depth explorative data analysis (EDA) and Deep Learning model development project. I analyzed datasets regarding Myopia and Heart Disease, performing data cleaning, visualization, and training predictive models to identify risk factors.",
            stack: ["Python", "Jupyter Notebook", "Pandas", "Scikit-Learn", "Deep Learning"],
            icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M22 12h-4l-3 9L9 3l-3 9H2"></path></svg>',
            link: "#"
        },
        "creative": {
            title: "Creative Lab (Pygame)",
            desc: "A collection of visual algorithms and mini-games built from scratch. Includes a RayCasting engine (rendering 3D worlds from 2D maps), a Snake AI that teaches itself to play, and particle simulations. A playground for math and logic.",
            stack: ["Python", "Pygame", "Algorithms", "Linear Algebra"],
            icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect x="2" y="6" width="20" height="12" rx="2"></rect><path d="M6 12h4"></path><path d="M8 10v4"></path><circle cx="17" cy="12" r="1.5"></circle></svg>',
            link: "#"
        },
        "system": {
            title: "System Identification",
            desc: "Academic research project focused on modeling complex dynamic systems. Using MATLAB, I performed black-box and grey-box identification to derive mathematical models from raw input-output data, validating them against real-world benchmarks.",
            stack: ["MATLAB", "System Theory", "Data Modeling", "LaTeX"],
            icon: '<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"></path><polyline points="3.27 6.96 12 12.01 20.73 6.96"></polyline><line x1="12" y1="22.08" x2="12" y2="12"></line></svg>',
            link: "#"
        }
    };

    const projectCards = document.querySelectorAll('.project-card');
    const modal = document.getElementById('project-modal');
    const closeModalBtn = document.querySelector('.close-modal');

    // Make sure elements exist before trying to access them
    if (modal && projectCards.length > 0) {
        // Elements to fill
        const mTitle = document.getElementById('m-title');
        const mDesc = document.getElementById('m-desc');
        const mStack = document.getElementById('m-stack');
        const mIcon = document.querySelector('.modal-icon');
        const mLink = document.getElementById('m-link');

        projectCards.forEach(card => {
            card.addEventListener('click', (e) => {
                e.stopPropagation(); // Prevent bubbling to the works tile
                const id = card.getAttribute('data-id');
                // console.log("Clicked card:", id); // Debug

                if (projectData[id]) {
                    const data = projectData[id];

                    // Fill Data
                    mTitle.innerText = data.title;
                    mDesc.innerText = data.desc;
                    mIcon.innerHTML = data.icon;

                    // Clear and Fill Stack
                    mStack.innerHTML = '';
                    data.stack.forEach(tech => {
                        const tag = document.createElement('span');
                        tag.innerText = tech;
                        mStack.appendChild(tag);
                    });

                    // Show Modal
                    modal.classList.remove('hidden');
                    // Small timeout to allow display:block to apply before opacity transition
                    setTimeout(() => {
                        modal.classList.add('active');
                    }, 10);
                }
            });
        });

        // Close Logic
        if (closeModalBtn) {
            closeModalBtn.addEventListener('click', () => {
                modal.classList.remove('active');
                setTimeout(() => {
                    modal.classList.add('hidden');
                }, 300);
            });
        }

        // Close on outside click
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                modal.classList.remove('active');
                setTimeout(() => {
                    modal.classList.add('hidden');
                }, 300);
            }
        });
        // --- EMAIL LINK FALLBACK ---
        // Force mailto via JS to bypass any potential anchor issues
        const emailLink = document.querySelector('a[href^="mailto:"]');
        if (emailLink) {
            emailLink.addEventListener('click', (e) => {
                e.stopPropagation(); // Stop bubbling
            });
        }
    }
});
