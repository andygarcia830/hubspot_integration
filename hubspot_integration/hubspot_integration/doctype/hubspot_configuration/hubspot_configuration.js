// Copyright (c) 2023, Xurpas Inc. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Hubspot Configuration", {
	refresh(frm) {
        frm.add_custom_button(
            __('Fetch New Won Deals'),function(){
                   
                    frappe.call({method:'hubspot_integration.hubspot_integration.doctype.hubspot_configuration.hubspot_configuration.fetch_won_deals', args:{
                              
                            },
                            callback:function(r){
                                //frm.reload_doc();
                            }
                            })
                        }
                
            
        );

        frm.add_custom_button(
            __('Fetch New Companies'),function(){
                   
                    frappe.call({method:'hubspot_integration.hubspot_integration.doctype.hubspot_configuration.hubspot_configuration.fetch_companies', args:{
                              
                            },
                            callback:function(r){
                                //frm.reload_doc();
                            }
                            })
                        }
                
            
        );

        

	},
});
