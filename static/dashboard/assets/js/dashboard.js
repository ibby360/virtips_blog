/*

=========================================================
* Volt Pro - Premium Bootstrap 5 Dashboard
=========================================================

* Product Page: https://themesberg.com/product/admin-dashboard/volt-premium-bootstrap-5-dashboard
* Copyright 2021 Themesberg (https://www.themesberg.com)

* Designed and coded by https://themesberg.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. Please contact us to request a removal. Contact us if you want to remove it.

*/

"use strict";
const d = document;
d.addEventListener("DOMContentLoaded", function (event) {

    const swalWithBootstrapButtons = Swal.mixin({
        customClass: {
            confirmButton: 'btn btn-primary me-3',
            cancelButton: 'btn btn-gray'
        },
        buttonsStyling: false
    });

    // options
    const breakpoints = {
        sm: 540,
        md: 720,
        lg: 960,
        xl: 1140
    };

    var preloader = d.querySelector('.preloader');
    if (preloader) {
        setTimeout(function () {
            preloader.classList.add('show');

            setTimeout(function () {
                d.querySelector('.loader-element').classList.add('hide');
            }, 200);
        }, 1000);
    }

    var sidebar = document.getElementById('sidebarMenu');
    var content = document.getElementsByClassName('content')[0];
    if (sidebar && d.body.clientWidth < breakpoints.lg) {
        sidebar.addEventListener('shown.bs.collapse', function () {
            document.querySelector('body').style.position = 'fixed';
        });
        sidebar.addEventListener('hidden.bs.collapse', function () {
            document.querySelector('body').style.position = 'relative';
        });
    }


    //Tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })

    // Popovers
    var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
    var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl)
    })


    // Choices.js
    var selectStateInputEl = d.querySelector('#state');
    if (selectStateInputEl) {
        const choices = new Choices(selectStateInputEl);
    }

    // Sortable Js
    if (d.body.clientWidth > breakpoints.lg) {
        var kanbanColumn1 = document.getElementById('kanbanColumn1');
        if (kanbanColumn1) {
            new Sortable(kanbanColumn1, {
                group: "shared",
            });
        }

        var kanbanColumn2 = document.getElementById('kanbanColumn2');
        if (kanbanColumn2) {
            new Sortable(kanbanColumn2, {
                group: "shared",
            });
        }

        var kanbanColumn3 = document.getElementById('kanbanColumn3');
        if (kanbanColumn3) {
            new Sortable(kanbanColumn3, {
                group: "shared",
            });
        }

        var kanbanColumn4 = document.getElementById('kanbanColumn4');
        if (kanbanColumn4) {
            new Sortable(kanbanColumn4, {
                group: "shared",
            });
        }
    }

    // multiple
    var selectStatesInputEl = d.querySelector('#states');
    if (selectStatesInputEl) {
        const choices = new Choices(selectStatesInputEl);
    }


    if (sidebar) {
        if (localStorage.getItem('sidebar') === 'contracted') {
            sidebar.classList.add('notransition');
            content.classList.add('notransition');

            sidebar.classList.add('contracted');

            setTimeout(function () {
                sidebar.classList.remove('notransition');
                content.classList.remove('notransition');
            }, 500);

        } else {
            sidebar.classList.add('notransition');
            content.classList.add('notransition');

            sidebar.classList.remove('contracted');

            setTimeout(function () {
                sidebar.classList.remove('notransition');
                content.classList.remove('notransition');
            }, 500);
        }

        var sidebarToggle = d.getElementById('sidebar-toggle');
        sidebarToggle.addEventListener('click', function () {
            if (sidebar.classList.contains('contracted')) {
                sidebar.classList.remove('contracted');
                localStorage.removeItem('sidebar', 'contracted');
            } else {
                sidebar.classList.add('contracted');
                localStorage.setItem('sidebar', 'contracted');
            }
        });

        sidebar.addEventListener('mouseenter', function () {
            if (localStorage.getItem('sidebar') === 'contracted') {
                if (sidebar.classList.contains('contracted')) {
                    sidebar.classList.remove('contracted');
                } else {
                    sidebar.classList.add('contracted');
                }
            }
        });

        sidebar.addEventListener('mouseleave', function () {
            if (localStorage.getItem('sidebar') === 'contracted') {
                if (sidebar.classList.contains('contracted')) {
                    sidebar.classList.remove('contracted');
                } else {
                    sidebar.classList.add('contracted');
                }
            }
        });
    }

});