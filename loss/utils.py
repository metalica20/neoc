def people_loss_notification(loss_people, status):
    peoples = []
    sms_message = []
    for people in loss_people:
        peoples.append('<tr><td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                       '<td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                       '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                       '<td  style="border: 1px solid black; border-collapse: collapse">%s</td></tr>'
                       % (people.status, people.name, people.count, people.gender))

    for stat in status:
        sms_message.append('\nNo of people %s is %d' % (stat['status'], stat['total']))
    email_message = """\
                <h3> People </h3>
                <table style="width:700px; border:1px solid black; text-align: center; border-collapse: collapse;">
                <tr>
                <th style="border: 1px solid black; border-collapse: collapse">Status</th>
                <th style="border: 1px solid black; border-collapse: collapse">Name</th>
                <th style="border: 1px solid black; border-collapse: collapse">Count</th>
                <th style="border: 1px solid black; border-collapse: collapse">Gender</th>
                </tr>
                %s
                </table>
              """ % (''.join(peoples))
    return email_message, ''.join(sms_message)


def family_loss_notification(loss_family, status):
    families = []
    sms_message = []
    for family in loss_family:
        families.append('<tr><td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                        '<td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                        '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                        '</tr>'
                        % (family.title, family.status, family.count))
    for stat in status:
        sms_message.append('\nNo of Family %s is %d' % (stat['status'], stat['total']))
    email_message = """\
               <h3> Family </h3>
                <table style="width:700px; border: 1px solid black;text-align: center; border-collapse: collapse;">
                <tr>
                <th style="border: 1px solid black; border-collapse: collapse">Owner Name</th>
                <th style="border: 1px solid black; border-collapse: collapse">Status</th>
                <th style="border: 1px solid black; border-collapse: collapse">Count</th>
                </tr>
                %s
                </table>
             """ % (''.join(families))
    return email_message, ''.join(sms_message)


def livestock_loss_notification(loss_livestock, status):
    livestocks = []
    sms_message = []
    for livestock in loss_livestock:
        livestocks.append('<tr><td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                          '<td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                          '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                          '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                          '<td  style="border: 1px solid black; border-collapse: collapse">%s</td></tr>'
                          % (
                              livestock.title, livestock.status, livestock.type,
                              livestock.count, livestock.economic_loss)
                          )
    for stat in status:
        sms_message.append('\nNo of Livestock %s is %d' % (stat['status'], stat['total']))
    email_message = """\
               <h3> Family </h3>
                <table style="width:700px; border: 1px solid black;text-align: center; border-collapse: collapse;">
                <tr>
                <th style="border: 1px solid black; border-collapse: collapse">Title</th>
                <th style="border: 1px solid black; border-collapse: collapse">Status</th>
                <th style="border: 1px solid black; border-collapse: collapse">Type</th>
                <th style="border: 1px solid black; border-collapse: collapse">Count</th>
                <th style="border: 1px solid black; border-collapse: collapse">Economic Loss</th>
                </tr>
                %s
                </table>
              """ % (''.join(livestocks))
    return email_message, ''.join(sms_message)


def infrastructure_loss_notification(loss_infrastructure, status):
    infrastructures = []
    sms_message = []
    for infrastructure in loss_infrastructure:
        infrastructures.append('<tr><td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                               '<td  style="border: 1px solid black; border-collapse: collapse">%s</td></tr>'
                               % (
                                   infrastructure.title, infrastructure.status, infrastructure.type,
                                   infrastructure.unit, infrastructure.equipment_value,
                                   infrastructure.infrastructure_value, infrastructure.count,
                                   infrastructure.beneficiary_owner, infrastructure.economic_loss)
                               )
    for stat in status:
        sms_message.append('\nNo of Infrastructure %s is %d' % (stat['status'], stat['total']))
    email_message = """\
               <h3> Family </h3>
                <table style="width:700px; border: 1px solid black;text-align: center; border-collapse: collapse;">
                <tr>
                <th style="border: 1px solid black; border-collapse: collapse">Title</th>
                <th style="border: 1px solid black; border-collapse: collapse">Status</th>
                <th style="border: 1px solid black; border-collapse: collapse">Type</th>
                <th style="border: 1px solid black; border-collapse: collapse">Unit</th>
                <th style="border: 1px solid black; border-collapse: collapse">Equipment Value</th>
                <th style="border: 1px solid black; border-collapse: collapse">Infrastructure Value</th>
                <th style="border: 1px solid black; border-collapse: collapse">Count</th>
                <th style="border: 1px solid black; border-collapse: collapse">Beneficiary Owner</th>
                <th style="border: 1px solid black; border-collapse: collapse">Economic Loss</th>
                </tr>
                %s
                </table>
             """ % (''.join(infrastructures))
    return email_message, ''.join(sms_message)


def agriculture_loss_notification(loss_agriculture, status):
    agricultures = []
    sms_message =[]
    for agriculture in loss_agriculture:
        agricultures.append('<tr><td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                            '<td style="border: 1px solid black; border-collapse: collapse">%s</td>'
                            '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                            '<td  style="border: 1px solid black; border-collapse: collapse">%s</td>'
                            '<td  style="border: 1px solid black; border-collapse: collapse">%s</td></tr>'
                            % (
                                agriculture.beneficiary_owner, agriculture.beneficiary_count, agriculture.type,
                                agriculture.status, agriculture.quantity)
                            )
    for stat in status:
        sms_message.append('\nAgriculture %s is %d %s' % (stat['status'], stat['total'], stat['type__unit']))
    email_message = """\
             <h3> Agriculture </h3>
             <table style="width:700px; border: 1px solid black;text-align: center; border-collapse: collapse;">
             <tr>
             <th style="border: 1px solid black; border-collapse: collapse">Owner</th>
             <th style="border: 1px solid black; border-collapse: collapse">Beneficiary Count</th>
             <th style="border: 1px solid black; border-collapse: collapse">Type</th>
             <th style="border: 1px solid black; border-collapse: collapse">Status</th>
             <th style="border: 1px solid black; border-collapse: collapse">Quantity</th>
             </tr>
             %s
             </table>
              """ % (''.join(agricultures))
    return email_message, ''.join(sms_message)
