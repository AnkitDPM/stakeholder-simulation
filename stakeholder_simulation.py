{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b0db1e64-ac68-4b67-9754-e165ad510602",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "366609f84cb243dd97e21ba6f168bdbc",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "SelectionSlider(description='Sim Runs:', index=2, options=(100, 200, 300, 400, 500, 600, 700, 800, 900, 1000),…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c9d0f46a8de246d1a5ec64a76743f19e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-Ego', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "206a1854e3d84bcb83f56b4dfa76d8ef",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-RiskAversion', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bfbaa711f414450e83a8489716eb7e58",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-StakeholderEngagement', index=1, options=('Low', 'Medium', 'High'), value='Me…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5c9e056a0bde48fe957b531757e84eb0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-Delays', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "64e18e7dc06d4e9ea665b7dd5e0a07c0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-ScopeCreep', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "36e5ca3a88ea434db390883f8e602912",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-Ego', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "7695a7330c3e4a11b1e05fe070bdfe9f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-RiskAversion', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "b2758d32358c439bb1f10967410689ed",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-StakeholderEngagement', index=1, options=('Low', 'Medium', 'High'), value='Medi…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "18436e5687c34ed7a9cc6f6bbda026f6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-Delays', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cd7f1a1161d04b1eb179747f23f1b483",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-ScopeCreep', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4ff32e31d7864ee680216db3888a326a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-Ego', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c0ef41479d384b40a7122211c008c240",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-RiskAversion', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "4d8b029f44454c7baecc26b4b2f93752",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-StakeholderEngagement', index=1, options=('Low', 'Medium', 'High'), value='Mediu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9a8851e1ae4b478b981d9a265f2e2b53",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-Delays', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "df1c26e026804b768f37ce0ea3e478da",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-ScopeCreep', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0b34143050674132b3ecf34396e9c572",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-Adaptability', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ba428b56c9294f97affc4a897a7efe83",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-CollaborativePlanning', index=1, options=('Low', 'Medium', 'High'), value='Me…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "361f305886394cb58d420e94c752de56",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-ConstructiveFeedback', index=1, options=('Low', 'Medium', 'High'), value='Med…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e15a236334b0459d883e9c6972c8d05a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-ProactiveComms', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ba5b176d7e53492ab588153fd4cabd90",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-ConflictResolution', index=1, options=('Low', 'Medium', 'High'), value='Mediu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "061a24d128ac41528d9916dfb3b64a86",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Initiation-Miscommunication', index=1, options=('Low', 'Medium', 'High'), value='Medium'…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "26917cee3f6e486cbc1e6be5c4d9be1d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-Adaptability', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c263c27609fd45f6bfca2a484fe1a504",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-CollaborativePlanning', index=1, options=('Low', 'Medium', 'High'), value='Medi…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a01065aba7c44daf892560620d6e88ee",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-ConstructiveFeedback', index=1, options=('Low', 'Medium', 'High'), value='Mediu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ef0a2bc22c5b43dab066e3955a104ff1",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-ProactiveComms', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "ee62ba3ef877483d977c6a4cf6a3e1de",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-ConflictResolution', index=1, options=('Low', 'Medium', 'High'), value='Medium'…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bbebe170126946f7a8a97656fb53dec8",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-Miscommunication', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "5e6bae79e4014a4880a3f3b1c6685be3",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-Adaptability', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "e137175eb0ac481b9859e44687a75183",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-CollaborativePlanning', index=1, options=('Low', 'Medium', 'High'), value='Med…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "46a7f81374bd4014a669fd393dd571cb",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-ConstructiveFeedback', index=1, options=('Low', 'Medium', 'High'), value='Medi…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "177bd6bed4a24793bc0253ba4f9842df",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-ProactiveComms', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "99cfd9731fe747c285f9591da9a4574d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-ConflictResolution', index=1, options=('Low', 'Medium', 'High'), value='Medium…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2bfee9a8c7cb43e298db6e7df18c2dfd",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-Miscommunication', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "0d9fba990b2645dcb2013b508de5c30a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-Adaptability', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a7d2f441ca1b470fb040943e25dec733",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-CollaborativePlanning', index=1, options=('Low', 'Medium', 'High'), value='Mediu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "aa7474df7d824366ae4f979a8d9a50f0",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-ConstructiveFeedback', index=1, options=('Low', 'Medium', 'High'), value='Medium…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "583c4fcc2e354c86aa737c3c0eaf2e7f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-ProactiveComms', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cd936d4142b54a619232c91397b0c3f9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-ConflictResolution', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "038c9872b6a14e67909517a56d14fedf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-Miscommunication', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "bbce7d8561604e8192f447e11da5b469",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-Adaptability', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "a02f7221b7b54847b41f27d4f49730e6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-CollaborativePlanning', index=1, options=('Low', 'Medium', 'High'), value='Medi…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "cf2578867de84570a3f462cad5c131c6",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-ConstructiveFeedback', index=1, options=('Low', 'Medium', 'High'), value='Mediu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8bbddc4174c24925bbfc5b2b7832985d",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-Delays', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c8ba92364ea74b17a2bcb346c12c279f",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Planning-Miscommunication', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "062c87c0724a47f2a2f9f290862fe3de",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-Adaptability', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "8dc46edf9a574ddd91fab0f553ab4126",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-CollaborativePlanning', index=1, options=('Low', 'Medium', 'High'), value='Med…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "95bd03c0d7f84ded95eb3540c9667503",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-ConstructiveFeedback', index=1, options=('Low', 'Medium', 'High'), value='Medi…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fc01cdbc150f441f83b1962042fe1fa7",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-Delays', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "9d79192ed5624eebb29ca5a585529b01",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Execution-Miscommunication', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "d551fbdf029a46adb302dd02b3ca19ba",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-Adaptability', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "fc14e0bb2d59400fbe04af502b07f317",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-CollaborativePlanning', index=1, options=('Low', 'Medium', 'High'), value='Mediu…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "2c5a58a47b994497b7fe7ce7a787617e",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-ConstructiveFeedback', index=1, options=('Low', 'Medium', 'High'), value='Medium…"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "c61d15024e014cd3a377600733ae12bf",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-Delays', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "f35bb3699d57420f8251dbe862c9ada9",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Dropdown(description='Closure-Miscommunication', index=1, options=('Low', 'Medium', 'High'), value='Medium')"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "6edc81372caa45618e1b44976fdde39a",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "Button(button_style='success', description='Run Simulation 🚀', style=ButtonStyle())"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "import plotly.express as px\n",
    "\n",
    "st.set_page_config(page_title=\"Stakeholder Simulation\", layout=\"wide\")\n",
    "\n",
    "# --- Roles, Phases, Behaviors ---\n",
    "phases = ['Initiation', 'Planning', 'Execution', 'Closure']\n",
    "roles_behaviors = {\n",
    "    \"Client\": {\n",
    "        \"phases\": ['Initiation', 'Planning', 'Closure'],\n",
    "        \"behaviors\": [\"Ego\", \"RiskAversion\", \"StakeholderEngagement\", \"Delays\", \"ScopeCreep\"]\n",
    "    },\n",
    "    \"Project Manager\": {\n",
    "        \"phases\": ['Initiation', 'Planning', 'Execution', 'Closure'],\n",
    "        \"behaviors\": [\"Adaptability\", \"CollaborativePlanning\", \"ConstructiveFeedback\", \"ProactiveComms\", \"ConflictResolution\", \"Miscommunication\"]\n",
    "    },\n",
    "    \"Project Team\": {\n",
    "        \"phases\": ['Planning', 'Execution', 'Closure'],\n",
    "        \"behaviors\": [\"Adaptability\", \"CollaborativePlanning\", \"ConstructiveFeedback\", \"Delays\", \"Miscommunication\"]\n",
    "    }\n",
    "}\n",
    "ordinal_levels = ['Low', 'Medium', 'High']\n",
    "ordinal_map = {'Low': 1, 'Medium': 2, 'High': 3}\n",
    "role_colors = {\n",
    "    \"Client\": \"#e3f2fd\",\n",
    "    \"Project Manager\": \"#c8e6c9\",\n",
    "    \"Project Team\": \"#fff9c4\"\n",
    "}\n",
    "\n",
    "st.title(\"🌈 Role-based Stakeholder Simulation\")\n",
    "\n",
    "# --- Sidebar for Simulation Settings ---\n",
    "st.sidebar.header(\"Simulation Settings\")\n",
    "num_projects = st.sidebar.select_slider(\n",
    "    \"Number of Simulation Runs (multiples of 100)\", options=[100,200,300,400,500,600,700,800,900,1000], value=300)\n",
    "st.sidebar.markdown(\"---\")\n",
    "\n",
    "# --- Input for Each Role ---\n",
    "st.header(\"Configure Stakeholder Behaviors\")\n",
    "profiles = []\n",
    "for role in roles_behaviors:\n",
    "    with st.expander(f\"{role}\", expanded=True):\n",
    "        for phase in roles_behaviors[role][\"phases\"]:\n",
    "            st.subheader(f\"{role} - {phase} Phase\")\n",
    "            for behavior in roles_behaviors[role][\"behaviors\"]:\n",
    "                val = st.selectbox(\n",
    "                    f\"{role} - {phase} - {behavior}\",\n",
    "                    ordinal_levels,\n",
    "                    key=f\"{role}-{phase}-{behavior}\",\n",
    "                    index=1\n",
    "                )\n",
    "                profiles.append({\"Role\": role, \"Phase\": phase, \"Behavior\": behavior, \"Value\": val})\n",
    "\n",
    "profiles_df = pd.DataFrame(profiles)\n",
    "\n",
    "# --- Run Simulation Button ---\n",
    "if st.button(\"Run Simulation 🚀\"):\n",
    "    # --- Simulate ---\n",
    "    projects = []\n",
    "    for _ in range(num_projects):\n",
    "        phase = np.random.choice(phases)\n",
    "        role_means = {}\n",
    "        for role in roles_behaviors:\n",
    "            if phase in roles_behaviors[role]['phases']:\n",
    "                subset = profiles_df[(profiles_df.Role == role) & (profiles_df.Phase == phase)]\n",
    "                for behavior in roles_behaviors[role]['behaviors']:\n",
    "                    v = subset[subset.Behavior == behavior]['Value'].values[0]\n",
    "                    role_means[f\"{role}_{behavior}\"] = ordinal_map[v]\n",
    "        # Assign random weights per role/behavior\n",
    "        cost_score = sum(v * np.random.uniform(-1, 1) for v in role_means.values())\n",
    "        duration_score = sum(v * np.random.uniform(-1, 1) for v in role_means.values())\n",
    "        quality_score = 10 - abs(cost_score) - abs(duration_score) + np.random.normal(0, 1)\n",
    "        cost_cat = 'High' if cost_score > 2 else 'Medium' if cost_score > 0 else 'Low'\n",
    "        duration_cat = 'High' if duration_score > 2 else 'Medium' if duration_score > 0 else 'Low'\n",
    "        quality_cat = 'High' if quality_score > 7 else 'Medium' if quality_score > 4 else 'Low'\n",
    "        projects.append({\n",
    "            'Phase': phase,\n",
    "            'CostScore': cost_score, 'DurationScore': duration_score, 'QualityScore': quality_score,\n",
    "            'CostCat': cost_cat, 'DurationCat': duration_cat, 'QualityCat': quality_cat\n",
    "        })\n",
    "    projects_df = pd.DataFrame(projects)\n",
    "\n",
    "    st.success(\"Simulation complete! See results below:\")\n",
    "\n",
    "    # --- Plots ---\n",
    "    col1, col2, col3 = st.columns(3)\n",
    "    for kpi, col in zip(['CostCat','DurationCat','QualityCat'], [col1, col2, col3]):\n",
    "        fig = px.histogram(projects_df, x=kpi, color='Phase', barmode='group',\n",
    "                           category_orders={kpi: ['Low','Medium','High']},\n",
    "                           title=f\"{kpi.replace('Cat','')} by Phase\",\n",
    "                           color_discrete_sequence=px.colors.sequential.Plasma_r)\n",
    "        fig.update_layout(bargap=0.2)\n",
    "        col.plotly_chart(fig, use_container_width=True)\n",
    "\n",
    "    # --- Heatmap ---\n",
    "    st.subheader(\"Heatmap of Quality Category by Phase\")\n",
    "    quality_pivot = pd.crosstab(projects_df['Phase'], projects_df['QualityCat'])\n",
    "    fig = px.imshow(quality_pivot.values, labels=dict(x=\"Quality Category\", y=\"Phase\", color=\"Count\"),\n",
    "                    x=quality_pivot.columns, y=quality_pivot.index,\n",
    "                    color_continuous_scale='Viridis', text_auto=True)\n",
    "    st.plotly_chart(fig, use_container_width=True)\n",
    "\n",
    "    # --- Show Dataframe (optional) ---\n",
    "    with st.expander(\"See Raw Simulation Data\"):\n",
    "        st.dataframe(projects_df)\n",
    "\n",
    "else:\n",
    "    st.info(\"Configure behaviors above, then click 'Run Simulation 🚀' to see results.\")\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
