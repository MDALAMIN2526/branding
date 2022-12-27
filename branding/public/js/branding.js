$(window).on('load', function() {
    frappe.after_ajax(function () {
        if (frappe.boot.branding_setting.show_help_menu) {
            // $('.dropdown-help').css('display','block');
            $('.dropdown-help').attr('style', 'display: block !important');
        }
        if (frappe.boot.branding_setting.logo_width) {
            $('.app-logo').css('width',frappe.boot.branding_setting.logo_width+'px');
        }
        if (frappe.boot.branding_setting.logo_height) {
            $('.app-logo').css('height',frappe.boot.branding_setting.logo_height+'px');
        }
        if (frappe.boot.branding_setting.navbar_background_color) {
            $('.navbar').css('background-color',frappe.boot.branding_setting.navbar_background_color)
        }
        if (frappe.boot.branding_setting.custom_navbar_title_style && frappe.boot.branding_setting.custom_navbar_title) {
            $(`<span style=${frappe.boot.branding_setting.custom_navbar_title_style.replace('\n','')} class="hidden-xs hidden-sm">${frappe.boot.branding_setting.custom_navbar_title}</span>`).insertAfter("#navbar-breadcrumbs")
        }
    })
})
