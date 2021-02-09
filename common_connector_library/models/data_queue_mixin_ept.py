from odoo import models


class DataQueueMixinEpt(models.AbstractModel):
    """ Mixin class for delete unused data queue from database."""
    _name = 'data.queue.mixin.ept'
    _description = 'Data Queue Mixin'

    def delete_data_queue_ept(self, queue_detail=[], is_delete_queue=False):
        """
        Method for Delete unused data queues from connectors.
        @author: Keyur Kanani
        :param queue_detail: ['sample_data_queue_ept1','sample_data_queue_ept2']
        :param is_delete_queue: Delete all data form queue table.
        :return: True
        """
        if queue_detail:
            try:
                for tbl_name in queue_detail:
                    if is_delete_queue:
                        self._cr.execute("""delete from %s """ % str(tbl_name))
                        continue
                    self._cr.execute(
                        """delete from %s where cast(create_date as Date) <= current_date - %d""" % (
                            str(tbl_name), 7))
            except Exception as e:
                return e
        return True
