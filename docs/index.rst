Ecosystem for Brain Modeling
============================

We are building an ecosystem for general-purpose brain modeling, evolving from our previously experimental `BrainPy project <https://github.com/brainpy/BrainPy>`_.
This ecosystem is a collection of tools, libraries, and frameworks that can be used to build brain dynamics models and applications.

The brain modeling ecosystem is designed to be modular, so you can use as much or as little of it as you need.

We welcome contributions from the community, so if you have an idea for a new tool or library, please let us know!

Please email us at: `chao.brain@qq.com <mailto:chao.brain@qq.com>`_.


.. contents::
    :local:
    :depth: 2


`brainunit`: Physical Units
------------------------------


.. image:: https://raw.githubusercontent.com/chaobrain/saiunit/main/docs/_static/brainunit.png
   :width: 250
   :alt: brainunit logo
   :align: center

Starting from `brainunit <https://github.com/chaobrain/brainunit>`_, we are going to develop a new ecosystem for brain dynamics programming.

`brainunit <https://github.com/chaobrain/brainunit>`_ provides comprehensive physical units and unit-aware mathematical system for brain dynamics. It is designed to be fully compatible with JAX's transformation systems, including ``jax.jit``, ``jax.grad``, ``jax.vmap``, ``jax.pmap``, and others.

`brainunit <https://github.com/chaobrain/brainunit>`_ provides more than 2000+ commonly used physical units, and 200+ mathematical operations taking aware of these units.

`brainunit <https://github.com/chaobrain/brainunit>`_ is very easy to use, and also very useful for brain dynamics programming. Since most brain dynamics models are based on physical equations, it is very important to use physical units to ensure the correctness of the models.

Resources related to ``brainunit``:

* The documentation for brainunit can be found in: `https://brainunit.readthedocs.io/ <https://brainunit.readthedocs.io/>`_






`braincell`: Biologically Detailed Brain Cell Modeling
------------------------------------------------------


.. image:: https://raw.githubusercontent.com/chaobrain/braincell/main/docs/_static/braincell.png
   :width: 250
   :alt: braincell logo
   :align: center

`braincell <https://github.com/chaobrain/braincell>`_ is a package for dendritic computation in our BDP ecosystem. It provides a set of tools for building dendritic computation models, including the construction of dendritic trees, the definition of dendritic compartments, and the implementation of various ions and channels in a neuron.

`braincell <https://github.com/chaobrain/braincell>`_ is designed to be highly parallel for dendritic modeling. The computation for compartments and neurons are all parallelized in the single device, thus providing the extraordinary performance.

Resources related to ``braincell``:


* The documentation for braincell can be found in: `https://braincell.readthedocs.io/ <https://braincell.readthedocs.io/>`_






`brainstate`: ``State``-based Compilation
-----------------------------------------


.. image:: https://raw.githubusercontent.com/chaobrain/brainstate/main/docs/_static/brainstate.png
   :width: 250
   :alt: brainstate logo
   :align: center



Brain dynamics is characterized by intrinsic memory-intensive computations. Most operations are element-wise computation and should be optimized by JIT compilation. Therefore, we are developing `brainstate <https://github.com/chaobrain/brainstate>`_ for a easy-to-use JIT transformation system for BDP.

``jax``\ 's JIT interface is hard to directly applied to highly complex brain dynamics. On the contrary,  `brainstate <https://github.com/chaobrain/brainstate>`_ provides a ``State``\ -based transformation system which is higy intuitive for compiling BDP models. `brainstate <https://github.com/chaobrain/brainstate>`_ now provides various commonly used transformation functions, including gradient computation, control flows, and JIT compilation.

It is the foundation for the new version of BDP ecosystem. 

Resources related to ``brainstate``:


* The documentation for brainstate can be found in: `https://brainstate.readthedocs.io/ <https://brainstate.readthedocs.io/>`_





`braintaichi`: Event-Driven Computation Framework
-------------------------------------------------

.. image:: https://raw.githubusercontent.com/chaobrain/braintaichi/main/docs/_static/braintaichi.png
   :width: 250
   :alt: braintaichi logo
   :align: center


Brain dynamics is characterized by event-driven sparse computations, which is not compatible with existing operators for matrix multiplication.

`braintaichi <https://github.com/chaobrain/braintaichi>`_ is designed for customizing event-driven operators in brain dynamics. It leverages `Taichi Lang <https://www.taichi-lang.org/>`_, a domain-specific language embedded in Python that helps easily write high-performance parallel programs in CPUs and GPUs, and can be embeded into JAX/XLA process.

Nowadays, `braintaichi <https://github.com/chaobrain/braintaichi>`_ provides two levels of interface: (1) It provides a framework for customizing event-driven brain dynamics operators. (2) It implements several commonly used operators, including even-driven matrix-vector multiplication, `just-in-time connectivity operators <https://arxiv.org/abs/2311.05106>`_, and common sparse routines.

Resources related to ``braintaichi``:

* The documentation for braintaichi can be found in: `https://braintaichi.readthedocs.io/ <https://braintaichi.readthedocs.io/>`_






`brainscale`: Scalable Online Learning
-----------------------------------------

.. image:: https://raw.githubusercontent.com/chaobrain/brainscale/main/docs/_static/brainscale.jpg
   :width: 250
   :alt: brainscale logo
   :align: center

`brainscale <https://github.com/chaobrain/brainscale>`_ provides a scalable online learning framework for brain dynamics. It achieve O(N) memory and computational complexity for SNN online computation, and O(N^2) complexity for RNN computation.

Resources related to ``brainscale``:

* The documentation for braintaichi can be found in: `https://brainscale.readthedocs.io/ <https://brainscale.readthedocs.io/>`_




`braintools`: Commonly Used Tools
------------------------------------



.. image:: https://raw.githubusercontent.com/chaobrain/braintools/main/docs/_static/braintools.jpg
   :width: 250
   :alt: braintools logo
   :align: center

`braintools <https://github.com/chaobrain/braintools>`_ is a collection of tools for brain dynamics programming. It provides a set of tools for analyzing brain dynamics.

Resources related to ``braintools``:


* The documentation for braintools can be found in: `https://braintools.readthedocs.io/ <https://braintools.readthedocs.io/>`_





.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: More Information

   citation.rst
   book.md





.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Documentation

   brainunit <https://brainunit.readthedocs.io/>
   braincell <https://braincell.readthedocs.io/>
   brainstate <https://brainstate.readthedocs.io/>
   braintaichi <https://braintaichi.readthedocs.io/>
   brainscale <https://brainscale.readthedocs.io/>
   braintools <https://braintools.readthedocs.io/>

