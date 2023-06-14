// Copyright (c) 2023, Xurpas Inc. and contributors
// For license information, please see license.txt

frappe.ui.form.on("Deal", {
	refresh(frm) {
        frm.add_custom_button(
            __('Create Sales Order'),function(){

                frappe.call({method:'hubspot_integration.hubspot_integration.doctype.deal.deal.fetch_customer', args:{
                    name:frm.doc.name1
                },
                callback:function(r){
                    console.log(r.message.name)
                    window.location = '/app/sales-order/new-sales-order-1?customer='+r.message.name+'&amount='+frm.doc.amount+'&transaction_date='+frm.doc.close_date+"&deal="+frm.doc.name+"&business_segment="+frm.doc.business_segment+"&naming_series="+frm.doc.naming_series
                }
                })
                
        }
                
            
        );
        

        
	},
});
