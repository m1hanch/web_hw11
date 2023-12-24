"""added user to model

Revision ID: 8bf53d20f912
Revises: 994a34ee39b0
Create Date: 2023-12-24 16:31:16.159774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8bf53d20f912'
down_revision: Union[str, None] = '994a34ee39b0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'contacts', 'users', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'contacts', type_='foreignkey')
    op.drop_column('contacts', 'user_id')
    # ### end Alembic commands ###
