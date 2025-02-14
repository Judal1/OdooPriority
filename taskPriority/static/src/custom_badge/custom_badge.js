/** @odoo-module **/

import { BadgeField, badgeField } from "@web/views/fields/badge/badge_field";
import {registry} from "@web/core/registry";

export class CustomBadge extends BadgeField {
    static template = "taskPriority.badge";
    static props = {
        ...BadgeField.props,
        color: {type:Number, optional: true},
    }
    setup(){
        super.setup()
    }
    get colorClass(){
        return "o_tag o_tag_color_" + this.props.color
    }
    className(){
        return `${this.colorClass} ${this.classFromDecoration}`
    }


}
export const customBadge = {
    ...badgeField,
    component: CustomBadge,
    extractProps({attrs}) {
        const props = badgeField.extractProps(...arguments);
        props.color = Number.parseInt(attrs.color);
        return props
    }
}

registry.category("fields").add("custom_badge", customBadge);
